#!/usr/bin/env python3

from enum import Enum

class TEXT_EN(Enum):
    WINDOW_TITLE = 'Takuzu game'

    MENU_GRID_TITLE = 'Grid'
    MENU_PLAY_TITLE = 'Play'
    MENU_ABOUT_TITLE = 'About'
    MENU_QUIT_TITLE = 'Quit'

    SUB_MENU_4BY4_TITLE = '4x4 grid'
    SUB_MENU_6BY6_TITLE = '6x6 grid'
    SUB_MENU_CUSTOM_GRID_TITLE = 'Chose grid size'
    SUB_MENU_DIFFICULTY_EASY_TITLE = 'Easy'
    SUB_MENU_DIFFICULTY_HARD_TITLE = 'Hard'
    SUB_MENU_RANDOM_GRID_TITLE = 'Random grid'
    SUB_MENU_GAME_RULES_TITLE = 'Game rules'
    SUB_MENU_CREATORS_TITLE = 'Creators'
    SUB_MENU_QUIT_TITLE = 'Quit'

    HOME_DESCRIPTION = "Select a grid to start a game. You can change difficulty in the 'Play' menu"

    GAME_GRID_COMPLETE_MESSAGE = 'Grid complete! '
    GAME_GRID_VALID_MESSAGE = 'Grid valid! '
    GAME_GRID_NOT_VALID_ERROR_MESSAGE = 'Grid not valid. '
    GAME_NUMBERS_DISTRIBUTION_ERROR_MESSAGE = 'Each line need to have same number of 1 and 0. '
    GAME_GRID_NOT_FILLED_ERROR_MESSAGE = 'Grid valid but not filled yet. '
    GAME_LENGTH_NUMBER_SEQUENCE_ERROR_MESSAGE = 'The grid contains at least a sequence of 3 same number. '
    GAME_LIVES = 'Lives '
    GAME_HINTS = 'Hints '
    GAME_DIFFICULTY = 'Difficulty '
    GAME_GRID_SIZE = 'Grid size '
    GAME_VERIFY = 'Verify '
    GAME_WIN_TITLE = 'You won the game! '
    GAME_WIN_MESSAGE = 'Congratulations, you solved the grid! '
    GAME_LOSE_TITLE = 'You lose. '
    GAME_LOSE_MESSAGE = 'You consumed all your lives, the game is over. '
    GAME_TRY_AGAIN_MESSAGE = 'Try again? '
    GAME_HINTS_SPLASH_MESSAGE = 'Hints and verification infos would be written here :) '
