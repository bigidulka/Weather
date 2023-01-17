import interface as i
import sys

class GUI(i.QtWidgets.QMainWindow, i.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)

        self.initGUI()

    def initGUI(self):
        self.setWindowFlag(i.Qt.WindowType.FramelessWindowHint)

        # hide and close buttons
        #self.close_button.clicked.connect(QApplication.instance().quit)

    def main(self):
        app = i.QtWidgets.QApplication(sys.argv)
        window = GUI()
        window.show()
        app.exec_()

if __name__ == '__main__':
    gui = GUI()
    gui.main()