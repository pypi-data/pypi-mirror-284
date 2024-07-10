/* Copyright 2018 The OpenXLA Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef XLA_CPU_FUNCTION_RUNTIME_H_
#define XLA_CPU_FUNCTION_RUNTIME_H_

#include <stdint.h>

#include <cassert>
#include <cstdlib>

namespace xla {
namespace cpu_function_runtime {

struct EncodedBufferInfo {
  uint64_t packed_kind_and_size = 0;
  uint32_t entry_param_number = -1;
  uint32_t result_param_number = -1;
};

// Stores information about one buffer used by an XLA:CPU compiled function.
// These buffers are used for holding inputs to the computation, outputs from
// the computation and as temporary scratch space.
class BufferInfo {
 public:
  // Creates a BufferInfo from a serialized encoding generated by `Encode`.
  explicit constexpr BufferInfo(const EncodedBufferInfo& encoded)
      : kind_(UnpackKind(encoded.packed_kind_and_size)),
        size_(UnpackSize(encoded.packed_kind_and_size)),
        entry_param_number_(encoded.entry_param_number),
        result_param_number_(encoded.result_param_number) {}

  // Returns true if this buffer stores a constant.  These never need to be
  // allocated by the runtime.
  bool is_constant() const { return kind() == Kind::kConstant; }

  // Returns true if this buffer stores an entry parameter.  These may or may
  // not need to be allocated by the runtime, depending on
  // XlaCompiledCpuFunction::AllocMode.
  bool is_entry_parameter() const {
    return kind() == Kind::kParameter && entry_param_number_ >= 0;
  }

  // Returns the entry parameter number of this buffer.
  uint32_t entry_parameter_number() const {
    assert(is_entry_parameter());
    return entry_param_number_;
  }

  void set_result_parameter_number(uint32_t param_number) {
    result_param_number_ = param_number;
  }

  bool is_result_parameter() const {
    // Note: the kind is not unique, e.g. could be a kTempBuffer, or a
    // kParameter if it is an in-out argument.
    return result_param_number_ >= 0;
  }

  uint32_t result_parameter_number() const {
    assert(is_result_parameter());
    return result_param_number_;
  }

  // Returns true if this buffer is temporary scratch space required by the XLA
  // computations.  These are always allocated by the runtime.
  bool is_temp_buffer() const { return kind() == Kind::kTempBuffer; }

  // Returns true if this buffer is allocated on the C stack or into registers.
  // These buffers are never allocated by the runtime.
  bool is_on_stack_buffer() const { return kind() == Kind::kOnStackBuffer; }

  // Returns the size for this buffer.
  uint64_t size() const { return size_; }

  // Encodes this BufferInfo into two 64 bit integers that can be used to
  // reconstruct the BufferInfo later using the constructor.  We need this
  // because we use BufferInfo in places where using protocol buffers would
  // negatively impact binary size.
  EncodedBufferInfo Encode() const {
    static_assert(sizeof(*this) == 16, "");
    EncodedBufferInfo ret;
    ret.packed_kind_and_size = Pack(kind(), size_);
    ret.entry_param_number = entry_param_number_;
    ret.result_param_number = result_param_number_;
    return ret;
  }

  bool operator==(const BufferInfo& buffer_info) const {
    if (kind() != buffer_info.kind() || size() != buffer_info.size()) {
      return false;
    }
    return !is_entry_parameter() ||
           entry_parameter_number() == buffer_info.entry_parameter_number();
  }

  // Factory methods:

  static BufferInfo MakeTempBuffer(uint64_t size) {
    return BufferInfo(Kind::kTempBuffer, size);
  }
  static BufferInfo MakeConstant(uint64_t size) {
    return BufferInfo(Kind::kConstant, size);
  }
  // Note: in-out parameters are possible by first creating an entry parameter
  // and then calling set_result_parameter_number().
  static BufferInfo MakeEntryParameter(uint64_t size,
                                       uint32_t entry_param_number) {
    return BufferInfo(Kind::kParameter, size, entry_param_number);
  }
  // Only used in tests. Here we use kTempBuffer but it is unimportant.
  static BufferInfo MakeResultParameter(uint64_t size,
                                        uint32_t result_param_number) {
    // Here we
    return BufferInfo(Kind::kTempBuffer, size, /*entry_param_number=*/-1,
                      result_param_number);
  }
  static BufferInfo MakeOnStackBuffer(uint64_t size) {
    return BufferInfo(Kind::kOnStackBuffer, size);
  }

 private:
  BufferInfo() = default;

  enum class Kind : uint64_t {
    kConstant,
    kTempBuffer,
    kParameter,
    kOnStackBuffer
  };

  Kind kind() const { return static_cast<Kind>(kind_); }

  explicit BufferInfo(Kind kind, uint64_t size)
      : BufferInfo(kind, size,
                   /*entry_param_number=*/-1,
                   /*result_param_number=*/-1) {}
  explicit BufferInfo(Kind kind, uint64_t size, uint32_t entry_param_number)
      : BufferInfo(kind, size, entry_param_number,
                   /*result_param_number=*/-1) {}
  explicit BufferInfo(Kind kind, uint64_t size, uint32_t entry_param_number,
                      uint32_t result_param_number)
      : kind_(kind),
        size_(size),
        entry_param_number_(entry_param_number),
        result_param_number_(result_param_number) {}

  static uint64_t Pack(Kind kind, uint64_t size) {
    return (static_cast<uint64_t>(size) << 2) | static_cast<uint64_t>(kind);
  }

  static inline constexpr Kind UnpackKind(uint64_t packed) {
    return static_cast<Kind>((packed << 62) >> 62);
  }

  static inline constexpr uint64_t UnpackSize(uint64_t packed) {
    return packed >> 2;
  }

  Kind kind_ : 2;
  uint64_t size_ : 62;
  int32_t entry_param_number_ = -1;
  int32_t result_param_number_ = -1;
};

// Align to 64-bytes, to mimic tsl::Allocator::kAllocatorAlignment.
inline constexpr size_t Align() { return 64; }

// The minimum alignment of buffers passed to XLA:CPU.
inline constexpr size_t MinAlign() { return 16; }

// When declaring variables that will be passed to an XLA instance as input via
// set_arg_data(), be it a regular input or a resource variable in the graph,
// the C++ variables must be aligned.
//
// Example usage:
//   XLA_ALIGN std::array<float, 4> arg_x;
//   XLA_ALIGN float arg_y;
//   xla_instance.set_arg_data(0, arg_x.date());
//   xla_instance.set_arg_data(0, &arg_y);
#define XLA_ALIGN alignas(xla::cpu_function_runtime::Align())

// AlignedBufferBytes returns the sum of the size of each buffer in
// `buffer_infos`, skipping constants, on-stack buffers and, if
// allocate_entry_params is false, entry parameters.  There are `n` entries in
// `buffer_infos`.  Each buffer is aligned to Align() byte boundaries.
size_t AlignedBufferBytes(const BufferInfo* buffer_infos, size_t n,
                          bool allocate_entry_params);

// MallocContiguousBuffers allocates buffers for use by the entry point
// generated by tfcompile.  There are `n` entries in `buffer_infos`.  If
// `annotate_initialized` is set, the allocated memory will be annotated as
// having been initialized - this is useful when allocating temporary buffers.
// If allocate_entry_params is true then allocates temp buffers and entry
// parameters, otherwise allocated only temp buffers.  Slots in `bufs`
// corresponding to unallocated buffers are set to nullptr.
//
// A single contiguous block of memory is allocated, and portions of it are
// parceled out into `bufs`, which must have space for `n` entries.  Returns
// the head of the allocated contiguous block, which should be passed to
// FreeContiguous when the buffers are no longer in use.
void* MallocContiguousBuffers(const BufferInfo* buffer_infos, size_t n,
                              bool allocate_entry_params, void** bufs,
                              bool annotate_initialized);

// FreeContiguous frees the contiguous block of memory allocated by
// MallocContiguousBuffers.
void FreeContiguous(void* contiguous);
}  // namespace cpu_function_runtime
}  // namespace xla

#endif  // XLA_CPU_FUNCTION_RUNTIME_H_
