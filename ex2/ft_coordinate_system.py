import math
import sys

def distance(coord_tuple) -> float:
    return sum(coord_tuple)

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

coord_1 = "1,2,3"
coord_2 = "abc,def,ghi"
print(f"Parsing valid coordinates: \"{coord_1}\"")
coordinate_game(coord_1)
print(f"Parsing invalid coordinates: \"{coord_2}\"")
coordinate_game(coord_2)
