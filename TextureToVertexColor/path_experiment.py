import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)

sys.path.insert(0, dir_path)

from utils.util_os import *
from utils.util_other import *
