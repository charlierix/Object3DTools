# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "split_glb_into_multi_obj 2.py"

# https://docs.blender.org/api/current/bpy.ops.html
# https://docs.blender.org/api/current/bpy.ops.wm.html      (search for obj_export)

# https://docs.blender.org/api/current/info_overview.html
# https://docs.blender.org/api/current/bpy.data.html
# https://docs.blender.org/api/current/bpy.types.Object.html#bpy.types.Object
# https://docs.blender.org/api/current/bpy.types.Mesh.html#bpy.types.Mesh

# This is a tester script that opens a .glb and exports each object as its own .obj
#
# This doesn't export materials and doesn't do anything with vertex colors
#
# This needs to be done for each object, since .obj doesn't support hierarchies.  If all objects get exported into the same
# .obj, shapelab turns them into a single combined object

# WARNING: This looks like it's auto creating cube

# to override bpy.context.active_object, you would pass {'active_object': object} to bpy.types.Context.temp_override

import os
import sys
import pathlib
import bpy

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)

sys.path.insert(0, dir_path)

from utils.util_os import *
from utils.util_other import *

#input_file = "D:\\models\\!research\\texture to vertex\\violin.glb"
input_file = "D:\\models\\!research\\texture to vertex\\cartoon_many_objects.glb"

output_folder = create_unique_folder(str(pathlib.PurePath(os.path.dirname(input_file)).joinpath(os.path.splitext(os.path.basename(input_file))[0])))

print("")
print("input file: " + input_file)
print("output folder" + output_folder)
print("")

# Load the file
open_file(input_file)

print("")

# Unselect all objects
for obj in bpy.data.objects:
    obj.select_set(False)

# Find objects that have a mesh
for obj in bpy.data.objects:
    # NOTE: Blender creates a cube every time (even with -b arg).  To fix this: open blender, delete the cube, File -> Defaults -> Save Startup File
    # if obj.name != "Cube" and obj.data is not None and obj.data.id_type == "MESH":

    if obj.data is not None and obj.data.id_type == "MESH":
        print("child name: " + obj.name + " | data.id_type: " + obj.data.id_type)

        obj.select_set(True)

        file_name = get_unique_filename(str(pathlib.PurePath(output_folder).joinpath(obj.name + ".obj")))
        export_selected_obj(obj, file_name)

        obj.select_set(False)

        print("")