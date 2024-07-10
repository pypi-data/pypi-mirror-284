/* Copyright 2017 The TensorFlow Authors. All Rights Reserved.

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

#ifndef TENSORFLOW_CORE_PLATFORM_CPU_FEATURE_GUARD_H_
#define TENSORFLOW_CORE_PLATFORM_CPU_FEATURE_GUARD_H_

namespace tensorflow {
namespace port {

// Called by the framework when we expect heavy CPU computation and we want to
// be sure that the code has been compiled to run optimally on the current
// hardware. The first time it's called it will run lightweight checks of
// available SIMD acceleration features and log warnings about any that aren't
// used.
void InfoAboutUnusedCPUFeatures();

}  // namespace port
}  // namespace tensorflow

#endif  // TENSORFLOW_CORE_PLATFORM_CPU_FEATURE_GUARD_H_
