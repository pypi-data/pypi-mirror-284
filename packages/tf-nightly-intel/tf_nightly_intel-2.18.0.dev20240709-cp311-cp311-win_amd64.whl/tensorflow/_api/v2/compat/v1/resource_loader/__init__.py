# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator2/generator/generator.py script.
"""Public API for tf._api.v2.resource_loader namespace
"""

import sys as _sys

from tensorflow.python.platform.resource_loader import get_data_files_path # line: 48
from tensorflow.python.platform.resource_loader import get_path_to_datafile # line: 99
from tensorflow.python.platform.resource_loader import get_root_dir_with_all_resources # line: 59
from tensorflow.python.platform.resource_loader import load_resource # line: 30
from tensorflow.python.platform.resource_loader import readahead_file_path # line: 129

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "resource_loader", public_apis=None, deprecation=True,
      has_lite=False)
