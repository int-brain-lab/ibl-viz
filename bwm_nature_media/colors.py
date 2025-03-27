import json
import pandas as pd

df = pd.read_csv("structures.csv")
print(f"Loaded {len(df)} rows from structures.csv")

meshes = [184, 500, 453, 1057, 677, 247, 669, 31, 972, 44, 714, 95, 254, 22, 541, 922, 698, 895, 1089, 703, 623, 343, 512]

colors = {}
for mesh in meshes:
    # get the row of DF where the id matches the mesh value
    row = df.loc[df['id'] == mesh]

    rgb_triplet = row["rgb_triplet"].values[0]  # Extract the list from the Series
    # The list is a string, so we need to convert it to a list of ints
    rgb_triplet = rgb_triplet[1:-1].split(", ")
    rgb_triplet = tuple(map(int, rgb_triplet))

    # add alpha
    rgb_triplet = (*rgb_triplet, 1)
    colors[mesh] = rgb_triplet

# Save a JSON mapping mesh ID to color
with open('./mesh_colors.json', 'w') as f:
    json.dump(colors, f)
