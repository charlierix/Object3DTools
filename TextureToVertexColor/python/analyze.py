# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "analyze.py" -- -f "D:\models\!research\texture to vertex\cartoon_many_objects.glb"

import os
import sys
import argparse
import pathlib
import bpy

# Inject current folder to in memory path so that the scripts in subfolders can be found and imported
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))        

from utils.filefolder import *
from utils.collections import *

# Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="The 3D object file to process (that is texture mapped)", required=True)

argv = sys.argv[sys.argv.index('--') + 1:]      # blender ignores everything after -- (those are args for python script)
args = parser.parse_known_args(argv)[0]

input_file = args.file

# Load the file
open_file(input_file)

# for obj in bpy.context.scene.objects:
#     col = obj.instance_collection     # returns None
#     print(obj.name + " [member of] " + col.name)



# for laycol in bpy.context.view_layer.layer_collection.children:
#     # TODO: need to recurse, since laycol could have more children layer collections
#     print(laycol.name + " | laycol is hidden: " + str(laycol.hide_viewport) + " | col is hidden: " + str(laycol.collection.hide_viewport) + " | col is rendered: " + str(laycol.collection.hide_render))

#     laycol.hide_viewport = False
#     laycol.collection.hide_viewport = False
#     laycol.collection.hide_render = False

#     print(laycol.name + " | laycol is hidden: " + str(laycol.hide_viewport) + " | col is hidden: " + str(laycol.collection.hide_viewport) + " | col is rendered: " + str(laycol.collection.hide_render))

# bpy.context.view_layer.update()


show_all_collections()





