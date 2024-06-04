# File to unit test classes and function to see if they act in an expected fashion

# Backend classes Unit testing
# -----------------------------------------------------------------------------------------
import backend

#   Batte_Grid Class

dimensions = (4,4)
battle_grid_info = [["G*P01","G*O01"],
                    ["G*___","G*___"]]
UT_player_characters = []
UT_opponent_characters = []

battle_grid = backend.battle_grid(dimensions, battle_grid_info, UT_player_characters,UT_opponent_characters,)