/* Copyright 2024 The OpenXLA Authors.

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
#ifndef XLA_SERVICE_CPU_ONEDNN_CONVOLUTION_REWRITER_H_
#define XLA_SERVICE_CPU_ONEDNN_CONVOLUTION_REWRITER_H_
#if defined(INTEL_MKL) && defined(ENABLE_ONEDNN_V3)

#include <optional>

#include "absl/algorithm/container.h"
#include "absl/status/statusor.h"
#include "xla/hlo/ir/hlo_instructions.h"
#include "xla/hlo/ir/hlo_module.h"
#include "xla/service/hlo_pass_interface.h"

namespace xla {
namespace cpu {

// This pass converts hlo convolution instructions into a single oneDNN
// operation and rewrites into custom calls.
class OneDnnConvolutionRewriter : public HloModulePass {
 public:
  absl::string_view name() const override {
    return "onednn-convolution-rewriter";
  }

  using HloPassInterface::Run;
  absl::StatusOr<bool> Run(
      HloModule* module,
      const absl::flat_hash_set<absl::string_view>& execution_threads) override;

  static bool ShouldRewrite(const HloInstruction* instr);
};

}  // namespace cpu
}  // namespace xla

#endif  // INTEL_MKL && ENABLE_ONEDNN_V3
#endif  // XLA_SERVICE_CPU_ONEDNN_CONVOLUTION_REWRITER_H_
