import bpy
import csv
from pathlib import Path
import bmesh

# Path to your CSV file
csv_file_path = Path(__file__).parent / "data/raw/uuid_mlapdv.csv"

# Offset origin
offset_origin = (-5700, -6600, -4000)
SCALE = 0.05

mesh = bpy.data.meshes.new(name="BaseSphere")
bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
base_sphere = bpy.context.object
mesh = base_sphere.data
bpy.ops.object.delete()  # Remove the temporary sphere


# Function to place spheres
def place_spheres_from_csv(csv_path, offset):
    # Create a base sphere once

    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            # Only use every 1000 rows
            if reader.line_num % 1000 != 0:
                continue

            if len(row) != 4:
                print(f"Skipping invalid row: {row}")
                continue

            _, x, y, z = row

            try:
                x, y, z = float(x), float(y), float(z)

                # Adjusting position by the offset
                adj_x = (x + offset[0]) / 1000
                adj_y = (y + offset[1]) / 1000
                adj_z = (z + offset[2]) / 1000

                # Duplicate the base sphere
                sphere = bpy.data.objects.new(name="Sphere", object_data=mesh)

                bpy.context.collection.objects.link(sphere)

                sphere.location = (adj_x, adj_y, adj_z)
                sphere.scale = (SCALE, SCALE, SCALE)
                print(f"Placed sphere at: {adj_x}, {adj_y}, {adj_z}")

                # Add the material to the new sphere
                material = bpy.data.materials.new(name=f"SphereMaterial_{sphere.name}")
                material.use_nodes = True
                bsdf = material.node_tree.nodes.get('Principled BSDF')
                if bsdf:
                    bsdf.inputs['Base Color'].default_value = (0, 1, 0, 1)  # Green color (RGBA)
                sphere.data.materials.append(material)

            except ValueError:
                print(f"Skipping row with invalid coordinates: {row}")


# Run the function
place_spheres_from_csv(csv_file_path, offset_origin)

print("Finished placing spheres.")
