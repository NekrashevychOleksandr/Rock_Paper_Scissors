
# AI bot responsible for making moves of NPC pieces
class AI_bot:

    def __init__(self):
        pass
    

# Represents characters on the grid
class character:
    def __init__(self, name, character_id, current_HP, max_HP, ATK, DEF, AGI, statuses, equipment):
        self.name = name
        self.character_id = character_id
        self.current_HP = current_HP
        self.max_HP = max_HP
        self.ATK = ATK
        self.DEF = DEF
        self.AGI = AGI
        self.statuses = statuses
        self.equipment = equipment



# Represents the battle enviorment, and keeps track of it's state
class battle_grid:
    
    def __init__(self, dimensions, grid_tile_info, player_characters, opponent_characters):
        self.dimensions = dimensions

        # example grid_tile_info element = "G*P01" 
        #G = Grass tile, character with id = 01 present on the tile
        self.grid_tile_info = grid_tile_info
        self.player_characters = player_characters
        self.opponent_characters = opponent_characters
        self.round_count = 0
        self.player_turn = True
        self.battle_end = False
        self.tile_selected = [-1,-1]


    # Updates character position
    def update_character_position(self,character_id, new_tile_position):

        # Loops through the grid looking for tile with matching character_id, removes it from the tile and adds it to the new tile
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):

                if self.grid_tile_info[i][j][2:] == character_id:
                    self.grid_tile_info[i][j] = self.grid_tile_info[i][j][:2] + "___"
                    self.grid_tile_info[new_tile_position[0]][new_tile_position[1]] = self.grid_tile_info[new_tile_position[0]][new_tile_position[1]][:2]+character_id 
        return


    # Removes character from the grid
    def remove_character(self, character_id):

        # Loops through the grid looking for tile with matching character_id, removes it from the tile
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):

                if self.grid_tile_info[i][j][2:] == character_id:
                    self.grid_tile_info[i][j] = self.grid_tile_info[i][j][:2] + "___"
                    
        return

    # Updates grid tile type 
    def update_tile_type(self, tile_position, new_tile_type):

        self.grid_tile_info[tile_position[0]][tile_position[1]] = new_tile_type + self.grid_tile_info[tile_position[0]][tile_position[1]][1:]
        return

    # Attempts to select tile
    def select_tile_attempt(self, tile_position):
        pass


        



