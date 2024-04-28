import os
import sys
import pathlib

input_file = "D:\\models\\!research\\texture to vertex\\violin.glb"
output_folder = str(pathlib.PurePath(os.path.dirname(input_file)).joinpath(os.path.splitext(os.path.basename(input_file))[0]))

path_info = pathlib.PurePath(input_file)
with_suffix = path_info.stem + "_" + str(7) + path_info.suffix

seven = 6