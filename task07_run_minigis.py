from minigis.readshp import read_shapefile_header

filename = "data/Test_Points/mongolia_places.shp"

try:

    header = read_shapefile_header(filename)

    print("Shapefile Header Information")

    for key, value in header.items():
        print(key, ":", value)

except FileNotFoundError:
    print("Shapefile not found")

except ValueError as error:
    print("Invalid file:", error)