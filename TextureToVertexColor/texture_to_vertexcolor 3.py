# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "texture_to_vertexcolor 3.py" -- "D:\models\!research\texture to vertex\violin.glb"

# https://docs.blender.org/api/current/bpy.data.html
# https://docs.blender.org/api/current/bpy.types.World.html#bpy.types.World

# https://docs.blender.org/api/current/bpy.types.Object.html#bpy.types.Object
# https://docs.blender.org/api/current/bpy.types.Mesh.html#bpy.types.Mesh

# https://docs.blender.org/api/current/bpy.context.html
# https://docs.blender.org/api/current/bpy.types.Scene.html#bpy.types.Scene
# https://docs.blender.org/api/current/bpy.types.RenderSettings.html#bpy.types.RenderSettings

# NOTE: Blender creates a cube every time (even with -b arg).  To fix this: open blender, delete the cube, File -> Defaults -> Save Startup File

import os
import sys
import pathlib
import bpy

# Inject current folder to in memory path so that the scripts in subfolders can be found and imported
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))        

from utils.baking import *
from utils.export import *
from utils.filefolder import *
from utils.meshwork import *

input_file = sys.argv[sys.argv.index("--") + 1]  # get arg after "--"
output_folder = create_unique_folder(str(pathlib.PurePath(os.path.dirname(input_file)).joinpath(os.path.splitext(os.path.basename(input_file))[0])))

print("")
print("   input file: " + input_file)
print("output folder: " + output_folder)
print("")

# Load the file
open_file(input_file)

print("")

# TODO: for thumbnails, the objects will also need to be invisible
# https://docs.blender.org/manual/en/latest/editors/3dview/viewport_render.html

# Unselect all objects (the export is only the selected objects, so make sure nothing is currently selected)
for obj in bpy.context.scene.objects:
    obj.select_set(False)

prep_environment_for_baking()

# Find objects that have a mesh
for obj in bpy.context.scene.objects:
    # NOTE: Blender creates a cube every time (even with -b arg).  To fix this: open blender, delete the cube, File -> Defaults -> Save Startup File
    # if obj.name != "Cube" and obj.data is not None and obj.data.id_type == "MESH":

    if is_mesh(obj):
        #print("child name: " + obj.name + " | data.id_type: " + obj.data.id_type)

        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        # Create more triangles
        subdivide_mesh(obj.data)

        # Create colors
        create_colorattrib(obj.name, obj.data)      # obj.data is the base class of ID, but this instance is a mesh

        # Bake
        bake_texture_to_vertexcolor()

        # Export as vertex colored .obj
        file_name = get_unique_filename(str(pathlib.PurePath(output_folder).joinpath(obj.name + ".obj")))
        export_selected_obj(file_name)

        obj.select_set(False)

        print("")