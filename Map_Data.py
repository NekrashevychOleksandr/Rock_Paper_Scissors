# Dictionary containing the effects on agility of each tile
tile_agility = { 
    "G": 0,   # Grass
    "D": 0,   # Dirt
    "W": -2,  # Water
    "M": -5   # Mountain
}

# AI bot responsible for making moves of NPC pieces
class AI_bot:
    def __init__(self):
        """
        Initialize the AI bot.
        """
        pass

# Represents characters on the grid
class Character:
    def __init__(self, titles, name, character_id, LVL, current_HP, max_HP, ATK, DEF, AGI, statuses, equipment):
        """
        Initialize a character.

        :param titles: Titles of the character.
        :param name: Name of the character.
        :param character_id: Unique identifier for the character.
        :param LVL: Level of the character.
        :param current_HP: Current HP of the character.
        :param max_HP: Maximum HP of the character.
        :param ATK: Attack value of the character.
        :param DEF: Defense value of the character.
        :param AGI: Agility value of the character.
        :param statuses: Status effects on the character.
        :param equipment: Equipment of the character.
        """
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
        self.has_turn = True

    def LVL_up(self):
        """
        Level up the character, increasing stats.
        """
        self.LVL += 1
        self.max_HP += 1 
        self.AGI += 1
        self.ATK += 1
        self.DEF += 1

    def take_damage(self, incoming_damage):
        """
        Apply damage to the character, reducing HP.

        :param incoming_damage: Amount of damage to take.
        """
        self.current_HP -= (incoming_damage - self.DEF)

        if self.current_HP < 0:
            self.is_Dead = True

    def receive_healing(self, incoming_heal):
        """
        Heal the character, increasing HP.

        :param incoming_heal: Amount of healing to receive.
        """
        self.current_HP += incoming_heal

        # Prevents "overhealing"
        if self.current_HP > self.max_HP:
            self.current_HP = self.max_HP

    def increase_max_HP(self, increase_in_Max_HP):
        """
        Increase the maximum HP of the character.

        :param increase_in_Max_HP: Amount to increase max HP.
        """
        self.max_HP += increase_in_Max_HP

    def increase_ATK(self, increase_in_ATK):
        """
        Increase the attack value of the character.

        :param increase_in_ATK: Amount to increase attack.
        """
        self.ATK += increase_in_ATK

    def increase_AGI(self, increase_in_AGI):
        """
        Increase the agility value of the character.

        :param increase_in_AGI: Amount to increase agility.
        """
        self.AGI += increase_in_AGI

    def increase_DEF(self, increase_in_DEF):
        """
        Increase the defense value of the character.

        :param increase_in_DEF: Amount to increase defense.
        """
        self.DEF += increase_in_DEF

    def decrease_max_HP(self, decrease_in_Max_HP):
        """
        Decrease the maximum HP of the character.

        :param decrease_in_Max_HP: Amount to decrease max HP.
        """
        self.max_HP -= decrease_in_Max_HP

        if self.max_HP < 1:
            self.max_HP = 1

    def decrease_ATK(self, decrease_in_ATK):
        """
        Decrease the attack value of the character.

        :param decrease_in_ATK: Amount to decrease attack.
        """
        self.ATK -= decrease_in_ATK

        if self.ATK < 0:
            self.ATK = 0

    def decrease_AGI(self, decrease_in_AGI):
        """
        Decrease the agility value of the character.

        :param decrease_in_AGI: Amount to decrease agility.
        """
        self.AGI -= decrease_in_AGI

        if self.AGI < 1:
            self.AGI = 1

    def decrease_DEF(self, decrease_in_DEF):
        """
        Decrease the defense value of the character.

        :param decrease_in_DEF: Amount to decrease defense.
        """
        self.DEF -= decrease_in_DEF

        if self.DEF < 0:
            self.DEF = 0

# Represents the battle environment, and keeps track of its state
class Battle_Grid:
    def __init__(self, grid_tile_info, player_characters, opponent_characters):
        """
        Initialize the battle grid.

        :param dimensions: Dimensions of the grid.
        :param grid_tile_info: Information about each tile in the grid.
        :param player_characters: List of player characters.
        :param opponent_characters: List of opponent characters.
        """
        self.dimensions = [len(grid_tile_info),len(grid_tile_info[0])]

        # example grid_tile_info element = "g01*P01" 
        # G01 = Grass tile, character with id = P01 present on the tile
        self.grid_tile_info = grid_tile_info
        self.player_characters = player_characters
        self.opponent_characters = opponent_characters
        self.round_count = 0
        self.player_turn = True
        self.battle_end = False
        self.tile_selected = False
        self.selected_tile_position = [-1, -1]
        self.available_move_tiles = None
        self.selected_character = None

    # Sets the turn to be the player's
    def set_turn_player(self):
        """
        Set the current turn to be the player's turn.
        """
        self.player_turn = True

    # Sets the turn to be the opponent's
    def set_turn_opponent(self):
        """
        Set the current turn to be the opponent's turn.
        """
        self.player_turn = False

    # Returns list of available moves for the given character and their position based on agility value
    def get_characters_available_moves(self, character_tile_position):
        """
        Get the list of available moves for the selected character.

        :param character_tile_position: Current position of the character on the grid.
        :return: List of available move positions.
        """
        available_moves = []

        # Calculate true agility considering the tile effect
        true_agility = self.selected_character.AGI + tile_agility[self.grid_tile_info[character_tile_position[0]][character_tile_position[1]][0]]

        # Makes sure true agility is always at least 1 (or else characters could get stuck on a tile if agility too low)
        if true_agility < 1:
            true_agility = 1
        
        # Initial moves based on true agility
        available_moves.append([character_tile_position[0] - 1, character_tile_position[1]])
        available_moves.append([character_tile_position[0] + 1, character_tile_position[1]])
        available_moves.append([character_tile_position[0], character_tile_position[1] + 1])
        available_moves.append([character_tile_position[0], character_tile_position[1] - 1])
        last_added_moves = available_moves.copy()

        # Determines all possible end tiles based on character agility
        for _ in range(true_agility - 1):
            for move in last_added_moves:
                temp_array = []
                temp_array.append([move[0] - 1, move[1]])
                temp_array.append([move[0] + 1, move[1]])
                temp_array.append([move[0], move[1] + 1])
                temp_array.append([move[0], move[1] - 1])

                # Combines the new moves with old moves but removes the duplicates
                available_moves = list(set(available_moves) | set(temp_array))
                last_added_moves = temp_array.copy()

        return available_moves.copy()

    # Attempts to select tile
    def select_tile_attempt(self, tile_position):
        """
        Attempt to select a tile and set the selected character if valid.

        :param tile_position: Position of the tile to select.
        """
        if self.grid_tile_info[tile_position[0]][tile_position[1]][4] == "P" and self.player_characters[int(self.grid_tile_info[tile_position[0]][tile_position[1]][5:7]) - 1].has_turn:
            self.tile_selected_position = tile_position
            self.tile_selected = True
            self.selected_character = self.player_characters[int(self.grid_tile_info[tile_position[0]][tile_position[1]][5:7]) - 1]
            self.available_move_tiles = self.get_characters_available_moves(self.tile_selected_position)
        return

    # Updates character position
    def update_character_position(self, new_tile_position):
        """
        Update the character's position on the grid.

        :param new_tile_position: New position to move the character to.
        """
        # Copies character id to new grid tile
        character_id = self.grid_tile_info[self.selected_tile_position[0]][self.selected_tile_position[1]][4:7]
        self.grid_tile_info[new_tile_position[0]][new_tile_position[1]][4:7] = character_id

        # Removes character id from the prior tile
        self.grid_tile_info[self.selected_tile_position[0]][self.selected_tile_position[1]][4:7] = "___"

        return

    # Attempts to make move from prior selected tile to newly selected tile, if selected tile is invalid unselect first tile
    def selected_tile_move_attempt(self, new_tile_position):
        """
        Attempt to move the selected character to a new tile.

        :param new_tile_position: Position of the new tile to move to.
        """
        if new_tile_position in self.available_move_tiles:
            if self.grid_tile_info[new_tile_position[0]][new_tile_position[1]][4:7] == "___":
                self.update_character_position(new_tile_position)
                self.selected_character.has_turn = False
                return
            elif self.grid_tile_info[new_tile_position[0]][new_tile_position[1]][4] == "E":
                enemy_character = self.opponent_characters[int(self.grid_tile_info[new_tile_position[0]][new_tile_position[1]][5:7]) - 1]
                enemy_character.take_damage(self.selected_character.ATK)
                self.selected_character.has_turn = False
                return
            else:
                self.tile_selected = False
                self.selected_tile_position = [-1, -1]
                self.available_move_tiles = None
                self.selected_character = None
                return
        else:
            self.tile_selected = False
            self.selected_tile_position = [-1, -1]
            self.available_move_tiles = None
            self.selected_character = None
            return
