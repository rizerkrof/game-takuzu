#!/usr/bin/env python3

import numpy as np
import math

def reshapeListToSquareGrid(targetList, order):
    gridSize = int(math.sqrt(len(targetList)))
    return np.reshape(np.array(targetList), (gridSize, gridSize), order).tolist()

def reshapeSquareGridToList(targetGrid):
    return np.reshape(np.array(targetGrid), (1, len(targetGrid)**2))[0].tolist()

def createCustomCheckerBoard(boardSize, tileSize):
    tileHeigth, tileWidth = tileSize
    return np.fromfunction(lambda i, j: (i//tileHeigth)%2 != (j//tileWidth)%2, boardSize).astype(int).astype(str)
