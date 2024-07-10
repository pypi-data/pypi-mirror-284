/* Copyright 2022 The TensorFlow Authors. All Rights Reserved.

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
#ifndef TENSORFLOW_CORE_PROFILER_LIB_CONTEXT_TYPES_H_
#define TENSORFLOW_CORE_PROFILER_LIB_CONTEXT_TYPES_H_

#include <cstdint>

#include "absl/base/macros.h"
#include "tsl/profiler/lib/context_types.h"

// TODO: b/323943471 - This macro should eventually be provided by Abseil.
#ifndef ABSL_DEPRECATE_AND_INLINE
#define ABSL_DEPRECATE_AND_INLINE()
#endif

namespace tensorflow {
namespace profiler {

using ContextType ABSL_DEPRECATE_AND_INLINE() =
    tsl::profiler::ContextType;  // NOLINT

ABSL_DEPRECATE_AND_INLINE()
inline const char* GetContextTypeString(
    tsl::profiler::ContextType context_type) {
  return tsl::profiler::GetContextTypeString(context_type);
}

ABSL_DEPRECATE_AND_INLINE()
inline tsl::profiler::ContextType GetSafeContextType(uint32_t context_type) {
  return tsl::profiler::GetSafeContextType(context_type);
}

}  // namespace profiler
}  // namespace tensorflow

#endif  // TENSORFLOW_CORE_PROFILER_LIB_CONTEXT_TYPES_H_
