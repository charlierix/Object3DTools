# https://docs.blender.org/api/current/bpy.types.ViewLayer.html#bpy.types.ViewLayer
# https://docs.blender.org/api/current/bpy.types.LayerCollection.html#bpy.types.LayerCollection
# https://docs.blender.org/api/current/bpy.types.Collection.html#bpy.types.Collection

import bpy

def show_all_collections():
    for laycol in bpy.context.view_layer.layer_collection.children:
        # Show this collection and recurse any children
        show_collection(laycol)

    bpy.context.view_layer.update()

def show_collection(laycol):
    # print(laycol.name + " | laycol is hidden: " + str(laycol.hide_viewport) + " | col is hidden: " + str(laycol.collection.hide_viewport) + " | col is rendered: " + str(laycol.collection.hide_render))

    laycol.hide_viewport = False

    col = laycol.collection
    if col is not None:
        col.hide_viewport = False
        col.hide_render = False

    # print(laycol.name + " | laycol is hidden: " + str(laycol.hide_viewport) + " | col is hidden: " + str(laycol.collection.hide_viewport) + " | col is rendered: " + str(laycol.collection.hide_render))

    for child_laycol in laycol.children:
        show_collection(child_laycol)