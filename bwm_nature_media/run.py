import bpy
import csv
import time

# Path to your CSV file
csv_file_path = './bwm_nature_media/data/raw/uuid_mlapdv.csv'

# Offset origin
offset_origin = (-5700, -6600, -4000)

# Scale factor
scale_factor = 0.01

# Get the scene collection
collection = bpy.context.scene.collection

# Create a base UV sphere mesh
mesh = bpy.data.meshes.new(name="BaseSphere")
bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
base_sphere = bpy.context.object
mesh = base_sphere.data
bpy.ops.object.delete()  # Remove the temporary sphere

# Store objects for batch linking
objects_to_link = []

def place_spheres_from_csv(csv_path, offset):
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if len(row) != 4:
                print(f"Skipping invalid row: {row}")
                continue

            _, x, y, z = row

            try:
                x, y, z = float(x), float(y), float(z)

                # Adjusting position by the offset
                adj_x = (x - offset[0]) / 1000
                adj_y = (y - offset[1]) / 1000
                adj_z = (z - offset[2]) / 1000

                # Create a new sphere object from the existing mesh
                sphere = bpy.data.objects.new(name="Sphere", object_data=mesh)

                # Set location and scale
                sphere.location = (adj_x, adj_y, adj_z)
                sphere.scale = (scale_factor, scale_factor, scale_factor)

                # Store for batch linking
                objects_to_link.append(sphere)

            except ValueError:
                print(f"Skipping row with invalid coordinates: {row}")

# Process the CSV file
place_spheres_from_csv(csv_file_path, offset_origin)

# Batch link objects to the scene
for obj in objects_to_link:
    collection.objects.link(obj)

# Update the view layer
bpy.context.view_layer.update()

print("Finished placing spheres.")
