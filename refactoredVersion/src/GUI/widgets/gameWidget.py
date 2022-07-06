#!/usr/bin/env python3

# import library
from PyQt5.QtWidgets            import QWidget, QAction, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore               import Qt
from PyQt5.QtGui                import QFont

# import config file
from src.config                 import config

# import custom enums
from src.enums.difficultyEnum   import DIFFICULTY
from src.enums.tileEnum         import TILE
from src.enums.textEnum         import TEXT

class GameWidget(QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game
        # grid layout
        self.gridButtonLayout = QGridLayout()
        # game infos labels
        self.difficultyLabel = QLabel()
        self.livesLabel = QLabel()
        self.hintsLabel = QLabel()
        self.gridLabel = QLabel()
        # game verification buttons
        self.hintsButton = QPushButton(TEXT.GAME_HINTS.value, self)
        self.verifyButton = QPushButton(TEXT.GAME_VERIFY.value, self)
        # infos label
        self.infosLabel = QLabel()

        self.initGameWidget()

    def initGameWidget(self):
        self.updateLabels()
        self.gridButtonLayout.setContentsMargins(config.boardMargin, 0, config.boardMargin, 0)
        self.updateGridButtonLayout()

        gameInfosLayout = QHBoxLayout()
        gameInfosLayout.addWidget(self.gridLabel)
        gameInfosLayout.addWidget(self.difficultyLabel)
        gameInfosLayout.addWidget(self.hintsLabel)
        gameInfosLayout.addWidget(self.livesLabel)

        self.hintsButton.setFixedSize(250, 100)
        self.hintsButton.clicked.connect(self.empty)
        self.verifyButton.setFixedSize(250, 100)
        self.verifyButton.clicked.connect(self.checkGridCompleted)
        verificationButtonsLayout = QHBoxLayout()
        verificationButtonsLayout.addWidget(self.hintsButton)
        verificationButtonsLayout.addWidget(self.verifyButton)

        self.infosLabel.setText(TEXT.GAME_HINTS_SPLASH_MESSAGE.value)
        self.infosLabel.setAlignment(Qt.AlignCenter)
        self.infosLabel.setStyleSheet('background-color : '+config.buttonZeroColor)
        self.infosLabel.setFont(QFont(config.font, 9))
        self.infosLabel.setFixedHeight(50)

        self.gameLayout = QVBoxLayout()
        self.gameLayout.addLayout(self.gridButtonLayout)
        self.gameLayout.addLayout(gameInfosLayout)
        self.gameLayout.addLayout(verificationButtonsLayout)
        self.gameLayout.addWidget(self.infosLabel)

        self.setLayout(self.gameLayout)

    def updateLabels(self):
        self.difficultyLabel.setText(TEXT.GAME_DIFFICULTY.value+': '+self.game.difficulty)
        self.livesLabel.setText(TEXT.GAME_LIVES.value+': '+str(self.game.lives))
        self.hintsLabel.setText(TEXT.GAME_HINTS.value+': '+str(self.game.hints))
        self.gridLabel.setText(TEXT.GAME_GRID_SIZE.value+': '+str(self.game.gridSize)+'x'+str(self.game.gridSize))

    def updateGridButtonLayout(self):
        # clear layout
        for i in reversed(range(self.gridButtonLayout.count())):
            self.gridButtonLayout.itemAt(i).widget().setParent(None)
        # fill layout with button
        for i in range(self.game.gridSize):
            for j in range(self.game.gridSize):
                buttonValue = self.game.grid[i*self.game.gridSize+j]
                button = QPushButton(buttonValue, self)
                button.clicked.connect(self.onClick)
                button.setFont(QFont (config.font, 20))
                # button.setFixedSize(100, 100) if self.game.gridSize == 6 else button.setFixedSize(150, 150)
                button.setFixedSize(config.gridSize/self.game.gridSize, config.gridSize/self.game.gridSize)
                if buttonValue != TILE.EMPTY.value:
                    button.setFont(QFont (config.font, 30))
                    button.setEnabled(False)
                    if buttonValue == TILE.ONE.value:
                        button.setStyleSheet(' color :'+config.buttonFontColor+'; background-color : '+config.buttonOneColor)
                    else:
                        button.setStyleSheet(' color :'+config.buttonFontColor+'; background-color : '+config.buttonZeroColor)
                self.gridButtonLayout.addWidget(button, i+1, j+1)

    def onClick(self):
        valeur = self.sender().text()
        index=self.gridButtonLayout.indexOf(self.sender())
        if valeur == TILE.EMPTY.value:
            self.sender().setText(TILE.ZERO.value)
            self.game.grid[index]=TILE.ZERO.value
            self.gridButtonLayout.itemAt(index).widget().setStyleSheet(' color :'+config.buttonFontColor+'; background-color : '+config.buttonZeroColor)
        elif valeur == TILE.ZERO.value:
            self.sender().setText(TILE.ONE.value)
            self.game.grid[index]=TILE.ONE.value
            self.gridButtonLayout.itemAt(index).widget().setStyleSheet(' color :'+config.buttonFontColor+'; background-color : '+config.buttonOneColor)
        else:
            self.sender().setText(TILE.EMPTY.value)
            self.game.grid[index]=TILE.EMPTY.value
            self.gridButtonLayout.itemAt(index).widget().setStyleSheet(' color :'+config.buttonFontColor+'; background-color : '+config.buttonEmptyColor)

    def checkGridCompleted(self):
        gridCompleted, message = self.game.checkGridCompleted()
        if gridCompleted:
            self.winPopup()
            return True
        else:
            if self.game.lives == 0:
                self.losePopup()
                return False
            self.game.lives -= 1
            self.livesLabel.setText(TEXT.GAME_LIVES.value+': '+str(self.game.lives))
            return False

    def winPopup(self):
        self.winPopup = QMessageBox(QMessageBox.Information, TEXT.GAME_WIN_TITLE.value, TEXT.GAME_WIN_MESSAGE.value)
        self.winPopup.show()
        self.winPopup.setStandardButtons(QMessageBox.Ok)

    def losePopup(self):
        self.losePopup = QMessageBox(QMessageBox.Information, TEXT.GAME_LOSE_TITLE.value, TEXT.GAME_LOSE_MESSAGE.value+'\n'+TEXT.GAME_TRY_AGAIN_MESSAGE.value)
        self.losePopup.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.losePopup.show()
        if self.losePopup.exec()==QMessageBox.Yes:
            self.game.initLivesAndHints()
            self.parent().newGame(self.game.gridSize, self.game.difficulty, self.game.random)
            self.losePopup.close()
        else:
            # go back to home page
            self.parent().setCentralWidget(self.parent().homePageWidget())
            self.losePopup.close()

    def empty(self):
        print(self.game.checkGridCompleted())
        pass
