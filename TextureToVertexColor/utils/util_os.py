import bpy
import os
import pathlib

# If the folder passed in doesn't exist, this creates it.  Otherwise tries suffixes until one doesn't exist, then creates it
# Returns the folder name that was created
def create_unique_folder(folder_name):
    for i in range(10000):
        name_proposed = folder_name
        if i > 0:
            name_proposed = name_proposed + "_" + str(i)

        if not os.path.exists(name_proposed):
            folder_name = name_proposed
            os.makedirs(folder_name)
            return folder_name
        
    raise Exception("Couldn't find a unique name for: " + folder_name)

# If the filename passed in already exists, this will try different suffixes until it finds one that doesn't
def get_unique_filename(file_name):
    for i in range(10000):
        name_proposed = file_name
        if i > 0:
            path_info = pathlib.PurePath(file_name)
            name_proposed = str(pathlib.PurePath(path_info.parents[0]).joinpath(path_info.stem + "_" + str(i) + path_info.suffix))

        if not os.path.isfile(name_proposed):
            return name_proposed
        
    raise Exception("Couldn't find a unique name for: " + file_name)

# Looks at the extension and calls the appropriate import function
# NOTE: I don't know what most of these file types are, so maybe some don't make sense (but then this script wouldn't be called for those)
def open_file(file_name):
    extension = pathlib.Path(file_name).suffix.lower()

    if extension in [".glb", ".gltf"]:
        bpy.ops.import_scene.gltf(filepath = file_name)

    elif extension == ".fbx":
        bpy.ops.import_scene.fbx(filepath = file_name)

    elif extension in [".obj", ".mtl"]:
        bpy.ops.wm.obj_import(filepath = file_name)

    elif extension in [".x3d", ".wrl"]:
        bpy.ops.import_scene.x3d(filepath = file_name)

    elif extension == ".abc":
        bpy.ops.wm.alembic_import(filepath = file_name)

    elif extension == ".dae":
        bpy.ops.wm.collada_import(filepath = file_name)

    elif extension == ".ply":
        bpy.ops.wm.ply_import(filepath = file_name)

    elif extension == ".stl":
        bpy.ops.wm.stl_import(filepath = file_name)

    elif extension == ".usd":
        bpy.ops.wm.usd_import(filepath = file_name)

    else:
        raise Exception("Unexpected extension: " + extension)