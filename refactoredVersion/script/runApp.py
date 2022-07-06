import sys
sys.path.insert(0, sys.path[0]+'/../')

from src.app import Application

if __name__ == "__main__":
    takuzuGame = Application()
    takuzuGame.runApp()
