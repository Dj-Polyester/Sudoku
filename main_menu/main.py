from main_menu import Ui_MainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow("easy")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())