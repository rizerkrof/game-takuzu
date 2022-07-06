#!/usr/bin/env python3
import sys
# setup application project root path folder
rootPath = sys.path[0]

# import libraries
from PyQt5.QtWidgets            import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore               import Qt
from PyQt5.QtGui                import QIcon, QPixmap

# import custom enum
from src.enums.pathEnum         import PATH
from src.enums.textEnum         import TEXT
from src.enums.imageNameEnum    import IMAGE_NAME

class HomePageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._initHomePageWidget()

    def _initHomePageWidget(self):
        homePageImagePath = rootPath+PATH.HOME_PAGE_IMAGES.value+IMAGE_NAME.HOME_PAGE_SPLASH_SCREEN_IMAGE.value
        homePageImage = QLabel()
        homePageImage.setPixmap(QPixmap(homePageImagePath))
        homePageImage.setAlignment(Qt.AlignCenter)

        title = QLabel(TEXT.WINDOW_TITLE.value)
        title.setStyleSheet('color :orangered ; font-size: 44px')
        title.setAlignment(Qt.AlignCenter)

        description = QLabel(TEXT.HOME_DESCRIPTION.value)
        description.setStyleSheet('color :orangered ; font-size: 24px')
        description.setAlignment(Qt.AlignCenter)

        homePageLayout = QVBoxLayout()
        homePageLayout.addWidget(title)
        homePageLayout.addWidget(homePageImage)
        homePageLayout.addWidget(description)

        self.setLayout(homePageLayout)
