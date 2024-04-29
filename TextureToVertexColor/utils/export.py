import bpy

# Exports the currently selected objects as a .obj
# It doesn't export materials, but does export vertex colors
# Make sure filename is the full path and filename ending in .obj
def export_selected_obj(filename):
    # A lot of these params are optional, this was just copied from the api webpage
    # When looking at the export dialog box in blender, it looks like some of these params are just related to controlling that view (like filter_ and display mode)
    bpy.ops.wm.obj_export(
        filepath = filename,
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
        sort_method = 'DEFAULT',
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
        export_colors = True,       # False
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
        filter_glob = '*.obj')     # '*.obj;*.mtl'

