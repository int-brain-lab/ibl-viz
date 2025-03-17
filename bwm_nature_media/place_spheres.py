import bpy
import csv

# Path to your CSV file
csv_file_path = './data/raw/uuid_mlapdv.csv'

# Offset origin
offset_origin = (-5700, -6600, -4000)


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
                adj_x = x - offset[0]
                adj_y = y - offset[1]
                adj_z = z - offset[2]

                # Create sphere
                bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(adj_x, adj_y, adj_z))
                print(f"Done with: {row}")

            except ValueError:
                print(f"Skipping row with invalid coordinates: {row}")


place_spheres_from_csv(csv_file_path, offset_origin)

print("Finished placing spheres.")
