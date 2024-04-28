# "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" -b -P "extract_texture.py"
# https://docs.blender.org/api/current/info_overview.html
# https://docs.blender.org/api/current/bpy.data.html
# https://docs.blender.org/api/current/bpy.types.BlendData.html#bpy.types.BlendData
# https://docs.blender.org/api/current/bpy.types.Material.html#bpy.types.Material
# https://docs.blender.org/api/current/bpy.types.Node.html#bpy.types.Node
# https://docs.blender.org/api/current/bpy.types.ShaderNodeTexImage.html
# https://docs.blender.org/api/current/bpy.types.Image.html#bpy.types.Image


import bpy
import os

input_file = "D:\\models\\!research\\texture to vertex\\alia_summer_outfit.glb"
output_folder = os.path.dirname(input_file) + "\\" + os.path.splitext(os.path.basename(input_file))[0]

print(input_file)
print(output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the .glb file
bpy.ops.import_scene.gltf(filepath=input_file)

# Iterate through images (these are referenced when saving at the bottom of this script)
print("")

print("bpy.data.images.keys:")
for img_key in bpy.data.images.keys():
    print(img_key)

print("")
print("")
print("")

# Iterate through materials
for mat in bpy.data.materials:
    print("")
    #print("material id_type: " + mat.id_type + " | name: " + mat.name)     # AttributeError: 'Material' object has no attribute 'id_type'
    print("material name: " + mat.name)

    if mat.use_nodes:
        for node in mat.node_tree.nodes:
            # node.type             Node type (deprecated, use bl_static_type or bl_idname for the actual identifier string)
            # node.bl_static_type   Node type (deprecated, use with care)

            print("node name: " + node.name + " | bl_description" + node.bl_description + " | bl_idname: " + node.bl_idname + " | bl_label: " + node.bl_label)

            if node.bl_idname == 'ShaderNodeTexImage':
                img = node.image
                print("image name: " + img.name + " | name_full: " + img.name_full + " | file_format: " + img.file_format + " | filepath: " + img.filepath + " | source: " + img.source)

                # The file isn't actually sitting in the temp folder yet.  Unpack will put them under %appdata% local
                img.unpack(method='USE_LOCAL')

                # Save the image to your output directory
                bpy.data.images[img.name].save_render(output_folder + "\\" + mat.name + " - " + img.name + ".png")