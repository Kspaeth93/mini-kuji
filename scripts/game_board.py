"""
Copyright (C) 2017 Kevin Spaeth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import math, random

# TODO: Add Description
class GameBoard:

    # Minimum dimension of the game board
    MIN_DIMENSION = 3
    # Maximum dimension of the game board
    MAX_DIMENSION = 5
    
    # TODO: Add Description
    game_board_dimension = None
    # TODO: Add Description
    game_board_lists = None
    # TODO: Add Description
    game_board_details = None
    # TODO: Add Description
    game_board = None

    def __init__(self, game_board_dimension):
        if game_board_dimension is None:
            self.game_board_dimension = 3
        else:
            if game_board_dimension < 3 or game_board_dimension > 5:
                print("Invalid game board dimension. Defaulting to 3.")
                self.game_board_dimension = 3
            else:
                self.game_board_dimension = game_board_dimension
        self.generate_game_board()

    # Genereates a game board using the current game board dimension
    def generate_game_board(self):
        self.game_board_lists = self.generate_game_board_lists()
        self.game_board_details = self.generate_game_board_details()
        self.game_board = self.update_game_board()

    # Generate lists consisting of game board values for each dimension of the game board
    def generate_game_board_lists(self):
        game_board_combos = self.generate_game_board_combos()
        game_board_lists = [None] * self.game_board_dimension
        game_board_values = [None] * (self.game_board_dimension ** 2) 
        for i in range(self.game_board_dimension ** 2):
            game_board_values[i] = game_board_combos[i][-2:]
        for i in range(self.game_board_dimension):
            temp_list = [None] * self.game_board_dimension
            for j in range(self.game_board_dimension):
                temp_list[j] = game_board_values[(i * self.game_board_dimension) + j]
            game_board_lists[i] = temp_list
        return game_board_lists

    # Generate combos consisting of a game board space and a game board value
    def generate_game_board_combos(self):
        game_board_spaces = list(range(self.game_board_dimension ** 2))
        game_board_values = list(range(self.game_board_dimension ** 2))
        random.shuffle(game_board_spaces)
        random.shuffle(game_board_values)
        game_board_combos = [None] * (self.game_board_dimension ** 2)
        for i in range(self.game_board_dimension ** 2):
            game_board_combos[i] = str(game_board_spaces[i] + 1).zfill(2) + "-" + str(game_board_values[i] + 1).zfill(2)
        game_board_combos.sort()
        return game_board_combos

    # TODO: Add Description
    def generate_game_board_details(self):
        game_board_seed = self.generate_game_board_seed()
        game_board_details = [None] * self.game_board_dimension
        for i in range(self.game_board_dimension):
            temp_list = [None] * self.game_board_dimension
            for j in range(self.game_board_dimension):
                if (i * self.game_board_dimension) + j + 1 == game_board_seed:
                    temp_list[j] = "S"
                else:
                    temp_list[j] = "NP"
            game_board_details[i] = temp_list
        return game_board_details

    # TODO: Add Description
    def generate_game_board_seed(self):
        game_board_seed = random.randrange(self.game_board_dimension ** 2) + 1
        return game_board_seed

    # TODO: Add Description
    def get_game_board_details_by_space(self, space):
        if space is None or space < 1 or space > (self.game_board_dimension ** 2):
            print("Invalid game board space.")
        else:
            game_board_dimension = math.ceil(space / self.game_board_dimension)
            game_board_space = space - ((game_board_dimension - 1) * self.game_board_dimension)
            return self.game_board_details[game_board_dimension - 1][game_board_space - 1]

    # TODO: Add Description
    def set_game_board_details_by_space(self, space, picked):
        if space is None or space < 1 or space > (self.game_board_dimension ** 2):
            print("Invalid game board space.")
        elif picked is None or picked.upper() != "P" or picked.upper() != "NP":
            print("Invalid game board data.")
        else:
            game_board_dimension = math.ceil(space / self.game_board_dimension)
            game_board_space = space - ((game_board_dimension - 1) * self.game_board_dimension)
            self.game_board_details[game_board_dimension - 1][game_board_space - 1] = picked.upper()

    # TODO: Add Description
    def update_game_board(self):
        x = 1 # TODO: Implementation
        game_board = [None] * self.game_board_dimension
        for i in range(self.game_board_dimension):
            temp_list = [None] * self.game_board_dimension
            for j in range(self.game_board_dimension):
                space_detail = self.get_game_board_details_by_space((i * self.game_board_dimension) + j)
                if space_detail != "NP":
                    temp_list[j] = "value"
                else:
                    temp_list[j] = "??"
            game_board[i] = temp_list
        return game_board

    # TODO: Add Description
    def print_game_board(self):
        x = 1 # TODO: Implementation
        for i in range(self.game_board_dimension):
            print(self.game_board[i])

    # Prints the full game board including hidden game board spaces and values
    def print_full_game_board(self):
        for i in range(self.game_board_dimension):
            print(self.game_board_lists[i])

    # TODO: Add Description
    def print_game_board_details(self):
        for i in range(self.game_board_dimension):
            print(self.game_board_details[i])

game_board = GameBoard(3) # DEBUG
game_board.print_full_game_board() # DEBUG
game_board.print_game_board_details() # DEBUG
game_board.print_game_board() # DEBUG