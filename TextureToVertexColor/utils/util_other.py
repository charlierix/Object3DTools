import bpy

# This searches the direct children of this object and returns the mesh or null
def get_child_mesh_ORIG(obj):
    for child in obj.children:
        print("child name: " + obj.name + " | type: " + child.id_type)

        if child.data is not None:
            print("data.id_type: " + child.data.id_type)

    return None

def get_child_mesh(obj):
    for child in obj.children:
        if child.data is not None and child.data.id_type == "MESH":
            print("child name: " + obj.name + " | type: " + child.id_type + " | data.id_type: " + child.data.id_type)
            return child

    return None

def export_selected_obj(obj, filename):
    print("exporting '" + filename + "'")
    return