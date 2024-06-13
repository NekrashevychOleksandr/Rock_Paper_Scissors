# File to unit test classes and function to see if they act in an expected fashion

# map_Data.py Unit testing
# -----------------------------------------------------------------------------------------
import map_Data

 # Initalization of map data classess
loaded_grid_tile_info = [
                    ["g01*___#__","g01*P01#01","g01*___#__","g01*___#__","d01*___#__","d01*___#__","g01*___#__","g01*P01#02"],
                    ["g01*___#__","g01*___#__","g01*___#__","g01*___#__","d01*P01#03","d01*___#__","g01*___#__","g01*___#__"],
                    ["g01*___#__","d01*___#__","g01*P01#04","g01*___#__","d01*___#__","d01*___#__","g01*___#__","d01*___#__"],
                    ["g01*___#__","g01*___#__","g01*___#__","g01*___#__","d01*___#__","d01*___#__","g01*___#__","g01*___#__"],
                    ["g01*___#__","g01*___#__","g01*___#__","g01*___#__","d01*___#__","d01*___#__","g01*E01#01","g01*___#__"],
                    ["g01*___#__","d01*___#__","g01*E01#02","g01*___#__","d01*___#__","d01*___#__","g01*___#__","g01*___#__"],
                    ["g01*___#__","g01*___#__","g01*___#__","g01*___#__","d01*___#__","d01*___#__","g01*___#__","g01*___#__"],
                    ["g01*E01#03","g01*___#__","g01*___#__","g01*___#__","d01*___#__","d01*___#__","g01*___#__","g01*___#__"]]




player_characters = []
enemy_characters = []

for tile_row in loaded_grid_tile_info:
    for tile in tile_row:
        if tile[4] == "E": 
            enemy_characters.append(map_Data.Character([], "Test Name", tile[7:10], 1, 5, 5, 1, 0, 1, [], []))
        elif tile[4] == "P":
            player_characters.append(map_Data.Character([], "Test Name", tile[7:10], 1, 5, 5, 1, 0, 1, [], []))
battle_grid = map_Data.Battle_Grid(loaded_grid_tile_info, player_characters, enemy_characters)

def test_map_Data_update_character_position():

    battle_grid.selected_tile = True
    battle_grid.selected_tile_position = [0,1]
    battle_grid.update_character_position([1,1])
    
    if battle_grid.grid_tile_info[1][1] == "g01*P01#01":
        print("\nmap_Data_update_character_position TEST 1: SUCCESS")
    else:
        print("\nmap_Data_update_character_position TEST 1: FAILED")

    battle_grid.selected_tile = True
    battle_grid.selected_tile_position = [0,7]
    battle_grid.update_character_position([6,0])

    if battle_grid.grid_tile_info[6][0] == "g01*P01#02":
        print("\nmap_Data_update_character_position TEST 2: SUCCESS")
    else:
        print("\nmap_Data_update_character_position TEST 2: FAILED")

    return


test_map_Data_update_character_position()


