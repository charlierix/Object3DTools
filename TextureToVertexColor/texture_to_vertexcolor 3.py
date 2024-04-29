# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "texture_to_vertexcolor 3.py" -- "D:\models\!research\texture to vertex\violin.glb"

# https://docs.blender.org/api/current/bpy.data.html
# https://docs.blender.org/api/current/bpy.types.World.html#bpy.types.World

# https://docs.blender.org/api/current/bpy.context.html
# https://docs.blender.org/api/current/bpy.types.Scene.html#bpy.types.Scene
# https://docs.blender.org/api/current/bpy.types.RenderSettings.html#bpy.types.RenderSettings

# https://docs.blender.org/api/current/bpy.types.BakeSettings.html#bpy.types.BakeSettings

import os
import sys
import pathlib
import bpy

# Inject current folder to in memory path so that the scripts in subfolders can be found and imported
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))        

from utils.util_baking import *
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

        # TODO: subdivide to get more triangles
            # edit mode -> edges -> subdivide
            # it looks like two subdivisions just makes ugly ridges, but one seems to make things better



        file_name = get_unique_filename(str(pathlib.PurePath(output_folder).joinpath(obj.name + ".obj")))

        print("child name: " + obj.name + " | data.id_type: " + obj.data.id_type)
        print("exporting '" + file_name + "'")

        obj.select_set(True)
        export_selected_obj(file_name)
        obj.select_set(False)

        print("")







