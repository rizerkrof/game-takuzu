#!/usr/bin/env python3

# import libraries
import random as rd
import numpy as np
import math

# import custom modules
from src.tools                  import gridTools

# import custom enum
from src.enums.difficultyEnum   import DIFFICULTY
from src.enums.tileEnum         import TILE
from src.enums.textEnum         import TEXT

class Game():
    def __init__(self):
        # game infos
        self.lives = None
        self.hints = None
        self.difficulty = None
        self.random = None

        # grid infos
        self.gridSize = None
        self.grid = []
        self.size4Grid = ["0","1","1","0","1","0","1","0","0","1","0","1","1","0","0","1"]
        self.size6Grid = ["1","0","0","1","1","0","1","0","1","0","1","0","0","1","1","0","0","1","1","1","0","1","0","0","0","0","1","0","1","1","0","1","0","1","0","1"]
        self.randomGrid = []

        self.initGame()

    def initGame(self, gridSize=4, difficulty=DIFFICULTY.EASY.value, random=False, visible=False):
        self.gridSize = gridSize
        self.difficulty = difficulty
        self.random = random
        if self.random: self.initRandomGrid()
        self.lives = self.initLivesAndHints()
        self.hints = self.initLivesAndHints()
        self.grid = [TILE.EMPTY.value for _ in range(self.gridSize**2)]
        # pre fill the grid with random samples
        for rIndex in rd.sample(range(self.gridSize**2), 12 if self.gridSize == 6 else 6):
            if self.random:
                self.grid[rIndex] = self.randomGrid[rIndex]
            else:
                self.grid[rIndex] = self.size4Grid[rIndex] if self.gridSize==4 else self.size6Grid[rIndex]

    def initLivesAndHints(self):
        return {
            DIFFICULTY.EASY.value: 6,
            DIFFICULTY.HARD.value: 3
        }.get(self.difficulty, 3)

    def checkGridCompleted(self):
        allVerifs = [
            self.checkGridFull(),
            self.checkGridSameNumberSequenceLength(),
            self.checkGridNumbersDistributionInLines(),
            self.checkGridNoIdenticalLines(self.getGridRows()),
            self.checkGridNoIdenticalLines(self.getGridCols())
        ]
        for verif, message in allVerifs:
            if not verif:
                return verif, message
        return True, TEXT.GAME_GRID_COMPLETE_MESSAGE.value

    def checkGridFull(self):
        if self.grid.count(TILE.EMPTY.value) == 0:
            return True, TEXT.GAME_GRID_VALID_MESSAGE.value
        else:
            return False, TEXT.GAME_GRID_NOT_FILLED_ERROR_MESSAGE.value

    def checkGridNumbersDistributionInLines(self):
        for line in self.getGridRows() + self.getGridCols():
            if line.count(TILE.EMPTY.ZERO.value) != line.count(TILE.ONE.value):
                return False, TEXT.GAME_GRID_NOT_VALID_ERROR_MESSAGE.value+TEXT.GAME_NUMBERS_DISTRIBUTION_ERROR_MESSAGE.value
        return True, TEXT.GAME_GRID_VALID_MESSAGE.value

    def checkGridSameNumberSequenceLength(self):
        for line in self.getGridRows() + self.getGridCols():
            lineString = ''.join(map(str, line))
            oneSequence = ''.join(map(str, [TILE.ONE.value for _ in range(3)])) # '111'
            zeroSequence = ''.join(map(str, [TILE.ZERO.value for _ in range(3)])) # '000'
            if lineString.find(oneSequence) != -1 or lineString.find(zeroSequence) != -1:
                return False, TEXT.GAME_GRID_NOT_VALID_ERROR_MESSAGE.value+TEXT.GAME_LENGTH_NUMBER_SEQUENCE_ERROR_MESSAGE.value
        return True, TEXT.GAME_GRID_VALID_MESSAGE.value

    def checkGridNoIdenticalLines(self, gridLines):
        listRowStrings = [''.join(map(str, row)) for row in gridLines]
        if len(listRowStrings) == len(set(listRowStrings)):
            return True, TEXT.GAME_GRID_VALID_MESSAGE.value
        else:
            return False, TEXT.GAME_GRID_NOT_VALID_ERROR_MESSAGE.value

    def getGridRows(self):
        return gridTools.reshapeListToSquareGrid(self.grid, 'C')

    def getGridCols(self):
        return gridTools.reshapeListToSquareGrid(self.grid, 'F')

    def initRandomGrid(self):
        initRandomGrid = gridTools.createCustomCheckerBoard((self.gridSize, self.gridSize), (self.gridSize/2, self.gridSize/2))
        self.grid = gridTools.reshapeSquareGridToList(initRandomGrid)
        while not self.checkGridCompleted()[0]:
            indexList = rd.sample(range(self.gridSize**2), 2)
            tmp = self.grid[indexList[0]]
            self.grid[indexList[0]] = self.grid[indexList[1]]
            self.grid[indexList[1]] = tmp
            if rd.randint(0, 1):
                self.grid = gridTools.reshapeSquareGridToList(self.getGridCols())
                print(self.getGridCols())
            else:
                self.grid = gridTools.reshapeSquareGridToList(self.getGridRows())
                print(self.getGridRows())
        self.randomGrid = self.grid
        print(self.randomGrid)
