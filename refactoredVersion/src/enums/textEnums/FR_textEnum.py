#!/usr/bin/env python3

from enum import Enum

class TEXT_FR(Enum):
    WINDOW_TITLE = 'Jeu du takuzu'

    MENU_GRID_TITLE = 'Grille'
    MENU_PLAY_TITLE = 'Jouer'
    MENU_ABOUT_TITLE = 'A propos'
    MENU_QUIT_TITLE = 'Quitter'

    SUB_MENU_4BY4_TITLE = 'grille 4x4'
    SUB_MENU_6BY6_TITLE = 'grille 6x6'
    SUB_MENU_CUSTOM_GRID_TITLE = 'Grid personnalisée'
    SUB_MENU_CUSTOM_GRID_MESSAGE = 'Entrer la taille de la grille (nombre pair requis, ex: 8): '
    SUB_MENU_DIFFICULTY_EASY_TITLE = 'Facile'
    SUB_MENU_DIFFICULTY_HARD_TITLE = 'Difficile'
    SUB_MENU_RANDOM_GRID_TITLE = 'Grille aléatoire'
    SUB_MENU_GAME_RULES_TITLE = 'Règles du jeu'
    SUB_MENU_CREATORS_TITLE = 'Createurs'
    SUB_MENU_QUIT_TITLE = 'Quitter'

    HOME_DESCRIPTION = "Selectionnez une grille pour commencer une partie. Vous pouvez changer la difficulté dans le menu 'Jouer'."

    GAME_GRID_COMPLETE_MESSAGE = 'Grille complète! '
    GAME_GRID_VALID_MESSAGE = 'Grille valide! '
    GAME_GRID_NOT_VALID_ERROR_MESSAGE = 'Grille non valide. '
    GAME_NUMBERS_DISTRIBUTION_ERROR_MESSAGE = 'Chaque ligne doit contenir le même nombre de 1 et de 0. '
    GAME_GRID_NOT_FILLED_ERROR_MESSAGE = 'Grille valide mais pas entièrement complété. '
    GAME_LENGTH_NUMBER_SEQUENCE_ERROR_MESSAGE = 'La contient une séquence de 3 ou plus même chiffre. '
    GAME_LIVES = 'vies '
    GAME_HINTS = 'indices '
    GAME_DIFFICULTY = 'Difficulté '
    GAME_GRID_SIZE = 'Taille de la grille '
    GAME_VERIFY = 'Verifier '
    GAME_WIN_TITLE = 'Vous avez gagné la partie! '
    GAME_WIN_MESSAGE = 'Félicitations! Vous avez résolu la grille! '
    GAME_LOSE_TITLE = 'Vous avez perdu. '
    GAME_LOSE_MESSAGE = 'Vous avez utilisé toutes vos vies, la partie est terminée. '
    GAME_TRY_AGAIN_MESSAGE = 'Voulez-vous recommencer? '
    GAME_HINTS_SPLASH_MESSAGE = 'Les indices et les informations seront écris ici :) '
