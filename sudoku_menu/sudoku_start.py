from sudoku import Ui_SudokuWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_SudokuWindow(sys.argv[1])
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())