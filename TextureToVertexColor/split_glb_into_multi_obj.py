# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "split_glb_into_multi_obj.py" -- "D:\models\!research\texture to vertex\violin.glb"

# https://docs.blender.org/api/current/bpy.ops.html
# https://docs.blender.org/api/current/bpy.ops.wm.html      (search for obj_export)
# https://docs.blender.org/api/current/bpy.data.html
# https://docs.blender.org/api/current/bpy.types.Object.html#bpy.types.Object
# https://docs.blender.org/api/current/bpy.types.Mesh.html#bpy.types.Mesh

# This is a tester script that opens a .glb and exports each object as its own .obj
#
# This doesn't export materials and doesn't do anything with vertex colors
#
# This needs to be done for each object, since .obj doesn't support hierarchies.  If all objects get exported into the same
# .obj, shapelab turns them into a single combined object

# to override bpy.context.active_object, you would pass {'active_object': object} to bpy.types.Context.temp_override

import os
import sys
import pathlib
import bpy

# Inject current folder to in memory path so that the scripts in subfolders can be found and imported
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))        

from utils.util_os import *
from utils.util_export import *

input_file = sys.argv[sys.argv.index("--") + 1]  # get arg after "--"
output_folder = create_unique_folder(str(pathlib.PurePath(os.path.dirname(input_file)).joinpath(os.path.splitext(os.path.basename(input_file))[0])))

print("")
print("   input file: " + input_file)
print("output folder: " + output_folder)
print("")

# Load the file
open_file(input_file)

print("")

# Unselect all objects (the export is only the selected objects, so make sure nothing is currently selected)
for obj in bpy.data.objects:
    obj.select_set(False)

# Find objects that have a mesh
for obj in bpy.data.objects:
    # NOTE: Blender creates a cube every time (even with -b arg).  To fix this: open blender, delete the cube, File -> Defaults -> Save Startup File
    # if obj.name != "Cube" and obj.data is not None and obj.data.id_type == "MESH":

    if obj.data is not None and obj.data.id_type == "MESH":
        file_name = get_unique_filename(str(pathlib.PurePath(output_folder).joinpath(obj.name + ".obj")))

        print("child name: " + obj.name + " | data.id_type: " + obj.data.id_type)
        print("exporting '" + file_name + "'")

        obj.select_set(True)
        export_selected_obj(file_name)
        obj.select_set(False)

        print("")