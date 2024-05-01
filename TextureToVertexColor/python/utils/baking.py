# https://docs.blender.org/api/current/bpy.types.BakeSettings.html#bpy.types.BakeSettings
# https://docs.blender.org/api/current/bpy.ops.object.html

import bpy

def prep_environment_for_baking():
    # Set world color to white
    bpy.data.worlds['World'].color = (1, 1, 1)

    # Set render engine to cycles
    bpy.context.scene.render.engine = 'CYCLES'

    # Change bake target to vertex colors
    bpy.context.scene.render.bake.target = 'VERTEX_COLORS'

def bake_texture_to_vertexcolor():
    bpy.ops.object.bake(type='DIFFUSE', target='VERTEX_COLORS', pass_filter={'COLOR', 'DIFFUSE'})