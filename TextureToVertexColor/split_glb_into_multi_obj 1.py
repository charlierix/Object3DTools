# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "split_glb_into_multi_obj 1.py"

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

import bpy
import os

input_file = "D:\\models\\!research\\texture to vertex\\violin.glb"
output_folder = os.path.dirname(input_file) + "\\" + os.path.splitext(os.path.basename(input_file))[0]

print("")
print("input file: " + input_file)
print("output folder" + output_folder)
print("")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the .glb file
bpy.ops.import_scene.gltf(filepath=input_file)

# Unselect all objects
for obj in bpy.data.objects:
    obj.select_set(False)

# print("")
# print("--- objects ---")

# # Iterate objects
# for obj in bpy.data.objects:
#     print(obj.name)

print("")
print("--- meshes ---")
for mesh in bpy.data.meshes:
    if mesh.name == "Cube":
        continue

    print(mesh.name)

    # TODO: select the mesh so that only this is exported
    #bpy.data.objects["Cube"].select_set(True)
    mesh.select_set(True)       # this function doesn't exist for mesh, but it does for object

    # A lot of these params are optional, this was just copied from the api webpage
    # When looking at the export dialog box in blender, it looks like some of these params are just related to controlling that view (like filter_ and display mode)
    bpy.ops.wm.obj_export(
        filepath = '',
        check_existing = True,
        filter_blender = False,
        filter_backup = False,
        filter_image = False,
        filter_movie = False,
        filter_python = False,
        filter_font = False,
        filter_sound = False,
        filter_text = False,
        filter_archive = False,
        filter_btx = False,
        filter_collada = False,
        filter_alembic = False,
        filter_usd = False,
        filter_obj = False,
        filter_volume = False,
        filter_folder = True,
        filter_blenlib = False,
        filemode = 8,
        display_type = 'DEFAULT',
        sort_method = '',
        export_animation = False,
        start_frame = -2147483648,
        end_frame = 2147483647,
        forward_axis = 'NEGATIVE_Z',
        up_axis = 'Y',
        global_scale = 1.0,
        apply_modifiers = True,
        export_eval_mode = 'DAG_EVAL_VIEWPORT',
        export_selected_objects = True,     # False
        export_uv = True,
        export_normals = True,
        
        #export_colors = True,       # False
        export_colors = False,
        
        export_materials = False,       # True
        export_pbr_extensions = False,
        path_mode = 'AUTO',
        export_triangulated_mesh = False,
        export_curves_as_nurbs = False,
        export_object_groups = False,
        export_material_groups = False,
        export_vertex_groups = False,
        export_smooth_groups = False,
        smooth_group_bitflags = False,
        filter_glob = '*.obj;*.mtl')



