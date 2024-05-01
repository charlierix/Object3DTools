# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "texture_to_vertexcolor.py" -- -s 1 -m True -f "D:\models\!research\texture to vertex\violin.glb"

# https://docs.blender.org/api/current/bpy.data.html
# https://docs.blender.org/api/current/bpy.types.World.html#bpy.types.World

# https://docs.blender.org/api/current/bpy.types.Object.html#bpy.types.Object
# https://docs.blender.org/api/current/bpy.types.Mesh.html#bpy.types.Mesh

# https://docs.blender.org/api/current/bpy.context.html
# https://docs.blender.org/api/current/bpy.types.Scene.html#bpy.types.Scene
# https://docs.blender.org/api/current/bpy.types.RenderSettings.html#bpy.types.RenderSettings

# NOTE: Blender creates a cube every time (even with -b arg).  To fix this: open blender, delete the cube, File -> Defaults -> Save Startup File

# Imports a texture mapped file, bakes to vertex colors and exports as .obj files (or single file based on -m option)

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
import argparse
import pathlib
import bpy

# Inject current folder to in memory path so that the scripts in subfolders can be found and imported
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))        

from utils.baking import *
from utils.export import *
from utils.filefolder import *
from utils.meshwork import *

# Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sub_count", help="Number of subdivisions (making extra triangles)", type=int, default=0)
parser.add_argument("-m", "--multi_obj", help="True: each object becomes its own .obj file.  False: a single .obj is created (argparse with bool is counterintuitive.  Don't pass -m for false, pass -m True for true.  Passing -m False will still be True)", type=bool, default=False)
parser.add_argument("-f", "--file", help="The 3D object file to process (that is texture mapped)", required=True)

argv = sys.argv[sys.argv.index('--') + 1:]      # blender ignores everything after -- (those are args for python script)
args = parser.parse_known_args(argv)[0]

input_file = args.file
output_folder = ""
if args.multi_obj:
    output_folder = create_unique_folder(str(pathlib.PurePath(os.path.dirname(input_file)).joinpath(os.path.splitext(os.path.basename(input_file))[0])))
else:
    output_folder = create_folder(str(pathlib.PurePath(os.path.dirname(input_file)).joinpath("vertex colored")))

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
        if args.sub_count > 0:
            subdivide_mesh(args.sub_count)

        # Create colors (for the bake to write to)
        create_colorattrib(obj.name, obj.data)

        # Bake
        bake_texture_to_vertexcolor()

        # Export as vertex colored .obj
        if args.multi_obj:
            file_name = get_unique_filename(str(pathlib.PurePath(output_folder).joinpath(obj.name + ".obj")))
            export_selected_obj(file_name)

        obj.select_set(False)
        print("")

# Create single .obj file if multi_obj param is false
if not args.multi_obj:
    # Select all meshes
    for obj in bpy.context.scene.objects:
        obj.select_set(False)       # everything should already be false, but it doesn't hurt to make sure
        if is_mesh(obj):
            obj.select_set(True)

    # Export the file
    file_name = get_unique_filename(str(pathlib.PurePath(output_folder).joinpath(os.path.splitext(os.path.basename(input_file))[0] + ".obj")))
    export_selected_obj(file_name)