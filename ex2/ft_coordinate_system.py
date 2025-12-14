import math
import sys

def distance(coord_tuple_1:tuple, coord_tuple_2:tuple) -> float:
    x_1, y_1, z_1 = coord_tuple_1
    x_2, y_2, z_2 = coord_tuple_2
    d = math.sqrt((x_2 - x_1) * (x_2 - x_1) + (y_2 - y_1) * (y_2 - y_1) + (z_2 - z_1) * (z_2 - z_1))
    print(f"Distance between {coord_tuple_1} and {coord_tuple_2}: {d}")
    return sum(coord_tuple_1)

def get_coordinate_from_str(coordinates: str):
    splitted_coord = coordinates.split(',')
    i = 0
    while (i < len(splitted_coord)):
        try:
            splitted_coord[i] = int(splitted_coord[i])
        except:
            print(f"Error parsing coordinates: invalid literal for int() with base 10: \'{splitted_coord[i]}\'")
            return
        i += 1
    return tuple(splitted_coord)

def coordinate_game(coordinate:str):
    tuple_coords = get_coordinate_from_str(coordinate)
    if (tuple_coords != None):
        print(f"Parsed position: {tuple_coords}")

coord_0 = "0,0,0"
tuple_0 = get_coordinate_from_str(coord_0)
print(f"Tuple 0 {tuple_0}")
coord_1 = "10,20,5"
coord_2 = "abc,def,ghi"
print(f"Parsing valid coordinates: \"{coord_1}\"")
tuple_1 = get_coordinate_from_str(coord_1)
print(f"Parsing invalid coordinates: \"{coord_2}\"")
coordinate_game(coord_2)
distance(tuple_0, tuple_1)

