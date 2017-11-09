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

import os, sys, pytest

# Add file path(s) to system-path at runtime
sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))  

import game_board

class TestGameBoardTest:

    @pytest.fixture
    def game_board_fixture(self):
        game_board_fixture = game_board.GameBoard(3)
        game_board_lists = [None] * 3
        game_board_lists[0] = ["01", "02", "03"]
        game_board_lists[1] = ["04", "05", "06"]
        game_board_lists[2] = ["07", "08", "09"]
        game_board_details = [None] * 3
        game_board_details[0] = ["P", "NP", "S"]
        game_board_details[1] = ["NP", "P", "NP"]
        game_board_details[2] = ["NP", "NP", "P"]
        game_board_fixture.game_board_lists = game_board_lists
        game_board_fixture.game_board_details = game_board_details
        return game_board_fixture

    def test_get_game_board_data_by_space(self, game_board_fixture):
        # Should return None since this is an invalid game board space
        game_board_space_details = game_board_fixture.get_game_board_details_by_space(0)
        assert game_board_space_details is None
        game_board_space_details = game_board_fixture.get_game_board_details_by_space(3)
        assert game_board_space_details == "S"
        game_board_space_details = game_board_fixture.get_game_board_details_by_space(6)
        assert game_board_space_details == "NP"
        game_board_space_details = game_board_fixture.get_game_board_details_by_space(9)
        assert game_board_space_details == "P"
        # Should return None since this is an invalid game board space
        game_board_space_details = game_board_fixture.get_game_board_details_by_space(10)
        assert game_board_space_details is None

    def test_set_game_board_data_by_space(self):
        x = 1 # TODO: Write Test
        assert x == 0

    def test_update_game_board(self):
        x = 1 # TODO: Write Test
        assert x == 0

    def test_print_game_board(self):
        x = 1 # TODO: Write Test
        assert x == 0

    def test_print_full_game_board(self):
        x = 1 # TODO: Write Test
        assert x == 0

    def test_print_game_board_details(self):
        x = 1 # TODO: Write Test
        assert x == 0