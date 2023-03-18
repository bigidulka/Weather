import sys

# my files
from location import Location
from translate import Translate
from weatherDataWAPI import WeatherDataWAPI

# pyqt6
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QSystemTrayIcon, QApplication, QWidget
from PyQt6.QtGui import QIcon, QAction, QGuiApplication


class createGUI(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('path/interface.ui', self)
        self.initGUI()

    def initGUI(self):
        # window options
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.set_bottom_right()

        # minimazed and close buttons
        self.close.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.hide.clicked.connect(self.toggle_tray)

        # tray
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogApplyButton))
        self.tray_icon.activated.connect(self.toggle_tray)

        # searching
        self.clear.clicked.connect(lambda: self.searchEdit.clear())
        self.search.clicked.connect(lambda: self.display_location(Location.get_coor_city(self.searchEdit.toPlainText().strip()))
                                    if self.searchEdit.toPlainText().strip() else self.text.setText("Empty"))
        self.search_location.clicked.connect(lambda: self.display_location(Location.get_location_by_ip()))

    def display_location(self, coordinates: tuple[float, float]) -> None:
        weather_data = WeatherDataWAPI(coordinates, 'ru')
        translator = Translate(Location.observation_time(coordinates), weather_data)

        for name, value in translator.get_translation().items():
            if value is not None:
                widget = getattr(self, name)
                widget.setText(str(value))

    def set_bottom_right(self) -> None:
        screen_size = QApplication.primaryScreen().geometry()
        app_size = QWidget.size(self)
        screen_without_toolbar_size = QApplication.primaryScreen().availableGeometry()
        self.move(screen_size.width()-app_size.width(),
                  (screen_size.height() - app_size.height()) - (screen_size.height() - screen_without_toolbar_size.height()))

    def toggle_tray(self) -> None:
        if self.isVisible():
            self.setVisible(False)
            self.tray_icon.show()
        else:
            self.setVisible(True)
            self.tray_icon.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = createGUI()
    window.show()
    app.exec()
