# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator2/generator/generator.py script.
"""Public API for tf._api.v2.io.gfile namespace
"""

import sys as _sys

from tensorflow.python.lib.io.file_io import copy_v2 as copy # line: 516
from tensorflow.python.lib.io.file_io import file_exists_v2 as exists # line: 249
from tensorflow.python.lib.io.file_io import get_registered_schemes # line: 980
from tensorflow.python.lib.io.file_io import get_matching_files_v2 as glob # line: 385
from tensorflow.python.lib.io.file_io import is_directory_v2 as isdir # line: 692
from tensorflow.python.lib.io.file_io import join # line: 781
from tensorflow.python.lib.io.file_io import list_directory_v2 as listdir # line: 751
from tensorflow.python.lib.io.file_io import recursive_create_dir_v2 as makedirs # line: 501
from tensorflow.python.lib.io.file_io import create_dir_v2 as mkdir # line: 470
from tensorflow.python.lib.io.file_io import delete_file_v2 as remove # line: 318
from tensorflow.python.lib.io.file_io import rename_v2 as rename # line: 609
from tensorflow.python.lib.io.file_io import delete_recursively_v2 as rmtree # line: 666
from tensorflow.python.lib.io.file_io import stat_v2 as stat # line: 911
from tensorflow.python.lib.io.file_io import walk_v2 as walk # line: 837
from tensorflow.python.platform.gfile import GFile # line: 36

from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "io.gfile", public_apis=None, deprecation=True,
      has_lite=False)
