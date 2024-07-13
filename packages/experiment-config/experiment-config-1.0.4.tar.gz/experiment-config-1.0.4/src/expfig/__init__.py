from .logging import make_sequential_log_dir, get_logger, TapeRecorder
from .core import nested_dict_update
from .namespacify import Namespacify
from .fig import Config

logger = get_logger()
tape = TapeRecorder()
