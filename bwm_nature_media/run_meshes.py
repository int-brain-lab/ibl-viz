import bpy
import os

# Path to your OBJ mesh folder
mesh_folder = "./bwm_nature_media/data/meshes/"
scale_factor = 0.001  # Scale down by 1000

# Function to create a transparent material
def create_transparent_material():
    mat = bpy.data.materials.new(name="TransparentMaterial")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Alpha"].default_value = 0.1  # 10% opacity
        mat.blend_method = 'BLEND'  # Enable transparency
        mat.use_transparent_shadow = False  # Disable shadows
        mat.use_backface_culling = False  # Double-sided rendering
    return mat

# Create transparent material once
transparent_mat = create_transparent_material()

meshes = [184, 500, 453, 1057, 677, 247, 669, 31, 972, 44, 714, 95, 254, 22, 541, 922, 698, 895, 1089, 703, 623, 343, 512]

# Import all OBJ files
for file in os.listdir(mesh_folder):
    if file.endswith(".obj") and int(file.split(".")[0]) in meshes:
        file_path = os.path.join(mesh_folder, file)
        bpy.ops.wm.obj_import(filepath=file_path)

        # Get last imported object
        imported_obj = bpy.context.selected_objects[0]

        if imported_obj and imported_obj.type == 'MESH':
            # Scale down the object
            imported_obj.scale = (scale_factor, scale_factor, scale_factor)

            # Assign transparent material
            if len(imported_obj.data.materials) == 0:
                imported_obj.data.materials.append(transparent_mat)
            else:
                imported_obj.data.materials[0] = transparent_mat

bpy.context.view_layer.update()
print("Finished importing, scaling, and applying transparency to all meshes!")
