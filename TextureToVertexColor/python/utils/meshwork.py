# https://docs.blender.org/api/current/bpy.ops.object.html
# https://docs.blender.org/api/current/bpy.types.Mesh.html#bpy.types.Mesh
# https://docs.blender.org/api/current/bpy.types.AttributeGroup.html#bpy.types.AttributeGroup

import bpy

def is_mesh(obj):
    return obj.data is not None and obj.data.id_type == "MESH"

# Splits the current mesh's triangles into multiple triangles
# 1 seems to be the best option, 2 starts looking like a quilt, 3+ are worse
# But, the more triangles, the more points to color, then smooth it out later
def subdivide_mesh(count):
    # edit mode -> edges -> subdivide

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action = 'SELECT')

    bpy.ops.mesh.subdivide(number_cuts = count)

    bpy.ops.object.mode_set(mode='OBJECT')

# Adds a color attrib to the mesh.  This is what the bake will write to
def create_colorattrib(obj_name, mesh):
    if mesh.color_attributes.active_color_index < 0:
        mesh.color_attributes.new(obj_name + "_color", "FLOAT_COLOR", "POINT")        # not sure if POINT is the same as vertex (otherwise, use CORNER)
        mesh.update()