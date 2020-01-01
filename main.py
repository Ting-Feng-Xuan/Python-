import os
import sys
from Game.game import Comoku
from PyQt5.QtWidgets import QApplication
from Game.windowshow import ComokuWindow

def main():

    # g = Comoku()
    # g.play()
    app = QApplication(sys.argv)
    ex = ComokuWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    path = os.getcwd()

    main()