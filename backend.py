
# AI bot responsible for making moves of NPC pieces
class AI_bot:

    def __init__(self):
        pass
    

# Represents characters on the grid
class character:
    def __init__(self, titles, name, character_id, LVL, current_HP, max_HP, ATK, DEF, AGI, statuses, equipment):
        self.titles = titles
        self.name = name
        self.character_id = character_id
        self.LVL = LVL
        self.current_HP = current_HP
        self.max_HP = max_HP
        self.ATK = ATK
        self.DEF = DEF
        self.AGI = AGI
        self.statuses = statuses
        self.equipment = equipment
        self.is_Dead = False
        
    def LVL_up(self):
        self.LVL += 1
        self.max_HP += 1 
        self.AGI += 1
        self.ATK += 1
        self.DEF += 1

    def attack_character(self,incoming_damage):
        self.current_HP -= (incoming_damage - self.DEF)
    
    def heal_character(self, incoming_heal):
        self.current_HP += incoming_heal

        # Prevents "overhealing"
        if self.current_HP > self.max_HP:
            self.current_HP = self.max_HP

    def increase_max_HP(self,increase_in_Max_HP):
        self.max_HP += increase_in_Max_HP

    def increase_ATK(self,increase_in_ATK):
        self.ATK += increase_in_ATK

    def increase_AGI(self,increase_in_AGI):
        self.AGI += increase_in_AGI

    def increase_DEF(self,increase_in_DEF):
        self.DEF += increase_in_DEF

    def decrease_max_HP(self,decrease_in_Max_HP):
        self.max_HP -= decrease_in_Max_HP

    def decrease_ATK(self,decrease_in_ATK):
        self.ATK -= decrease_in_ATK

    def decrease_AGI(self,decrease_in_AGI):
        self.AGI -= decrease_in_AGI

    def decrease_DEF(self,decrease_in_DEF):
        self.DEF -= decrease_in_DEF




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
        self.tile_selected = False
        self.tile_selected_position = [-1,-1]


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

        if self.grid_tile_info[tile_position[0]][tile_position[1]][2] == "P":
            self.tile_selected_position = tile_position
            self.tile_selected = True
        return
    
    # Attempts to make move from prior selected tile to newly selected tile
    def selected_tile_move_attempt(self, new_tile_position):

        if self.grid_tile_info[new_tile_position[0]][new_tile_position[1]][2] == "P":
            pass

        


        



