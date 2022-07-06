#!/usr/bin/env python3
import sys
# setup application project root path folder
rootPath = sys.path[0]

# import libraries
from PyQt5.QtWidgets                import QMainWindow, QAction, QMessageBox
from PyQt5.QtCore                   import QCoreApplication, Qt, QSize
from PyQt5.QtGui                    import QIcon, QKeySequence

# import custom modules
from src.game                       import Game
from src.GUI.widgets.gameWidget     import GameWidget
from src.GUI.widgets.homePageWidget import HomePageWidget

# import config file
from src.config                     import config

# import custom enums
from src.enums.difficultyEnum       import DIFFICULTY
from src.enums.pathEnum             import PATH
from src.enums.textEnum             import TEXT
from src.enums.imageNameEnum        import IMAGE_NAME
from src.enums.keyBindingsEnum      import KEY_BINDINGS

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TEXT.WINDOW_TITLE.value)
        self.setGeometry(300, 300, config.windowWidth, config.windowHeight)

        self.game = Game()

        self.setCentralWidget(self.homePageWidget())

        self._initMenuBar()

    def homePageWidget(self):
        return HomePageWidget()

    def gameWidget(self):
        return GameWidget(self.game)

    def _initMenuBar(self):
        menuBar = self.menuBar()

        gridMenu = menuBar.addMenu(TEXT.MENU_GRID_TITLE.value)
        gridMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_4BY4_TITLE.value, IMAGE_NAME.SUB_MENU_4BY4_ICON.value, KEY_BINDINGS.SUB_MENU_4BY4_SHORT_CUT.value, lambda: self.newGame(4, self.game.difficulty, self.game.random)))
        gridMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_6BY6_TITLE.value, IMAGE_NAME.SUB_MENU_6BY6_ICON.value, KEY_BINDINGS.SUB_MENU_6BY6_SHORT_CUT.value, lambda: self.newGame(6, self.game.difficulty, self.game.random)))
        gridMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_CUSTOM_GRID_TITLE.value, IMAGE_NAME.SUB_MENU_CUSTOM_GRID_ICON.value, KEY_BINDINGS.SUB_MENU_CUSTOM_GRID_SHORT_CUT.value, self.empty))
        playMenu = menuBar.addMenu(TEXT.MENU_PLAY_TITLE.value)
        playMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_DIFFICULTY_EASY_TITLE.value, IMAGE_NAME.SUB_MENU_DIFFICULTY_EASY_ICON.value, KEY_BINDINGS.SUB_MENU_DIFFICULTY_EASY_SHORT_CUT.value, lambda: self.newGame(self.game.gridSize, DIFFICULTY.EASY.value, self.game.random)))
        playMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_DIFFICULTY_HARD_TITLE.value, IMAGE_NAME.SUB_MENU_DIFFICULTY_HARD_ICON.value, KEY_BINDINGS.SUB_MENU_DIFFICULTY_HARD_SHORT_CUT.value, lambda: self.newGame(self.game.gridSize, DIFFICULTY.HARD.value, self.game.random)))
        playMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_RANDOM_GRID_TITLE.value, IMAGE_NAME.SUB_MENU_RANDOM_GRID_ICON.value, KEY_BINDINGS.SUB_MENU_RANDOM_GRID_SHORT_CUT.value, lambda: self.newGame(self.game.gridSize, self.game.difficulty, True)))
        aboutMenu = menuBar.addMenu(TEXT.MENU_ABOUT_TITLE.value)
        aboutMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_GAME_RULES_TITLE.value, IMAGE_NAME.SUB_MENU_GAME_RULES_ICON.value, KEY_BINDINGS.SUB_MENU_GAME_RULES_SHORT_CUT.value, self._showGameRules))
        aboutMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_CREATORS_TITLE.value, IMAGE_NAME.SUB_MENU_CREATORS_ICON.value, KEY_BINDINGS.SUB_MENU_CREATORS_SHORT_CUT.value, self.empty))
        quitMenu = menuBar.addMenu(TEXT.MENU_QUIT_TITLE.value)
        quitMenu.addAction(self._subMenuAction(TEXT.SUB_MENU_QUIT_TITLE.value, IMAGE_NAME.SUB_MENU_QUIT_ICON.value, KEY_BINDINGS.SUB_MENU_QUIT_SHORT_CUT.value, QCoreApplication.instance().quit))

    def _subMenuAction(self, title, icon, keybinding, functionOnClick):
        iconPath = rootPath+PATH.SUB_MENU_ICONS.value+icon
        subMenuAction = QAction(QIcon(iconPath), title, self)
        print(functionOnClick)
        subMenuAction.triggered.connect(functionOnClick)
        subMenuAction.setShortcut(QKeySequence(keybinding))
        return subMenuAction

    def _showGameRules(self):
        gameRulesPath = rootPath+PATH.GAME_RULES.value
        gameRules = open(gameRulesPath).read()
        self.rulesPopup = QMessageBox(QMessageBox.Information, TEXT.SUB_MENU_GAME_RULES_TITLE.value, gameRules)
        self.rulesPopup.show()

    def empty(self):
        pass

    def newGame(self, gridSize, difficulty, random):
        self.game.initGame(gridSize, difficulty, random)
        gameWidget = self.gameWidget()
        gameWidget.updateLabels()
        gameWidget.updateGridButtonLayout()
        self.setCentralWidget(gameWidget)
        pass
