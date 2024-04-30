# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "texture_to_vertexcolor.py" -- "D:\models\!research\texture to vertex\violin.glb"

# https://docs.blender.org/api/current/bpy.data.html
# https://docs.blender.org/api/current/bpy.types.World.html#bpy.types.World

# https://docs.blender.org/api/current/bpy.types.Object.html#bpy.types.Object
# https://docs.blender.org/api/current/bpy.types.Mesh.html#bpy.types.Mesh

# https://docs.blender.org/api/current/bpy.context.html
# https://docs.blender.org/api/current/bpy.types.Scene.html#bpy.types.Scene
# https://docs.blender.org/api/current/bpy.types.RenderSettings.html#bpy.types.RenderSettings

# NOTE: Blender creates a cube every time (even with -b arg).  To fix this: open blender, delete the cube, File -> Defaults -> Save Startup File

# Imports a texture mapped file, bakes to vertex colors and exports as .obj files

# This also does a subdivide to get more triangles (since only the verticies get colors, extra vertices means better color)
# I tried bumping up the subdivisions, but it looks really bad (like a waffle iron).  I wonder if smoothing steps between
# subdivisions would fix that

# I couldn't find an option for exporting vertex colors to .glb.  If that's possible, then all the objects could be done into
# a single file, preserving the initial hierarchy

# This needs to be done for each object, since .obj doesn't support hierarchies.  If all objects get exported into the same
# .obj, shapelab turns them into a single combined object

# TODO: It would be nice to generate a .png for each exported .obj.  When doing this, all other objects would probably need
# to be invisible when taking a picture (would also need to move the camera for each object)
# https://docs.blender.org/manual/en/latest/editors/3dview/viewport_render.html

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

# Unselect all objects (the export is only the selected objects, so make sure nothing is currently selected)
for obj in bpy.context.scene.objects:
    obj.select_set(False)

prep_environment_for_baking()

# Find objects that have a mesh
for obj in bpy.context.scene.objects:
    if is_mesh(obj):
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        # Create more triangles
        subdivide_mesh(obj.data)        # obj.data is the base class of ID, but this instance is a mesh

        # Create colors (for the bake to write to)
        create_colorattrib(obj.name, obj.data)

        # Bake
        bake_texture_to_vertexcolor()

        # Export as vertex colored .obj
        file_name = get_unique_filename(str(pathlib.PurePath(output_folder).joinpath(obj.name + ".obj")))
        export_selected_obj(file_name)

        obj.select_set(False)
        print("")