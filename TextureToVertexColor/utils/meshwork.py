# https://docs.blender.org/api/current/bpy.ops.object.html
# https://docs.blender.org/api/current/bpy.types.Mesh.html#bpy.types.Mesh
# https://docs.blender.org/api/current/bpy.types.AttributeGroup.html#bpy.types.AttributeGroup

import bpy

def is_mesh(obj):
    return obj.data is not None and obj.data.id_type == "MESH"

def subdivide_mesh(mesh):
    # edit mode -> edges -> subdivide
    # it looks like two subdivisions just makes ugly ridges, but one seems to make things better

    # --------------------------------------------

    # Edit Mode invalidates previous references from Object Mode, so be sure to reaquire them


    # mesh = bpy.context.active_object.data
    # polygons = mesh.polygons
    # bpy.ops.object.mode_set(mode='EDIT')
    # bpy.ops.object.mode_set(mode='OBJECT')

    # # this will crash
    # print(polygons)


    # mesh = bpy.context.active_object.data
    # polygons = mesh.polygons
    # bpy.ops.object.mode_set(mode='EDIT')
    # bpy.ops.object.mode_set(mode='OBJECT')

    # # polygons have been re-allocated
    # polygons = mesh.polygons
    # print(polygons)

    # --------------------------------------------

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action = 'SELECT')

    bpy.ops.mesh.subdivide(number_cuts = 1)         # seems to be the best option
    #bpy.ops.mesh.subdivide(number_cuts = 2)        # starts looking like a quilt
    #bpy.ops.mesh.subdivide(number_cuts = 3)        # looks really bad
    #bpy.ops.mesh.subdivide(number_cuts = 4)        # even worse

    bpy.ops.object.mode_set(mode='OBJECT')

def create_colorattrib(obj_name, mesh):
    if mesh.color_attributes.active_color_index < 0:
        mesh.color_attributes.new(obj_name + "_color", "FLOAT_COLOR", "POINT")        # not sure if POINT is the same as vertex (otherwise, use CORNER)
        mesh.update()