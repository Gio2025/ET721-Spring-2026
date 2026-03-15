"""
George Athanasopoulos
Unit Test Project – Drop Chip Game
Part 2 – pytest
ET721 Software Development Practicum
"""

from main import Connect4


def test_switch_player_x_to_o():
    game = Connect4()
    game.current_player = 'X'

    game.switch_player()

    assert game.current_player == 'O'


def test_switch_player_o_to_x():
    game = Connect4()
    game.current_player = 'O'

    game.switch_player()

    assert game.current_player == 'X'


def test_switch_player_multiple_times():
    game = Connect4()

    game.switch_player()
    assert game.current_player == 'O'

    game.switch_player()
    assert game.current_player == 'X'

