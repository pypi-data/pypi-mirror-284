# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Gradients for operators defined in state_ops.py."""

from tensorflow.python.framework import ops


# TODO(b/31222613): These ops may be differentiable, and there may be
# latent bugs here.
ops.NotDifferentiable("Assign")


ops.NotDifferentiable("AssignAdd")


ops.NotDifferentiable("AssignSub")


ops.NotDifferentiable("ScatterAdd")


ops.NotDifferentiable("ScatterSub")


ops.NotDifferentiable("ScatterMul")


ops.NotDifferentiable("ScatterDiv")


ops.NotDifferentiable("ScatterNdUpdate")

ops.NotDifferentiable("ScatterNdAdd")

ops.NotDifferentiable("ScatterNdSub")

ops.NotDifferentiable("ScatterNdMul")

ops.NotDifferentiable("ScatterNdDiv")
