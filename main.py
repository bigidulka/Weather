import sys

# my files
from location import Location
from translate import Translate
from weatherDataWAPI import WeatherData

# pyqt6
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QSystemTrayIcon, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton
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
        self.tray_icon.setIcon(self.style().standardIcon(
            QtWidgets.QStyle.StandardPixmap.SP_DialogApplyButton))
        self.tray_icon.activated.connect(self.toggle_tray)

        # searching
        self.clear.clicked.connect(lambda: self.searchEdit.clear())
        self.search.clicked.connect(lambda: self.display_location(Location.get_coor_city(self.searchEdit.toPlainText().strip()))
                                    if self.searchEdit.toPlainText().strip() else self.text.setText("Empty"))
        self.search_location.clicked.connect(
            lambda: self.display_location(Location.get_location_by_ip()))

    def on_daily_forecast_button_clicked(self, date_str):
        hourly_forecast_fr = self.translator.parse_hourly_forecast(date_str)

        # Clear the existing layout
        layout = self.hourly_scrollAreaCont.layout()
        if layout is not None:
            QWidget().setLayout(layout)

        # Create a new layout and add widgets to it
        layout = QHBoxLayout(self.hourly_scrollAreaCont)
        for fr_date, fr in hourly_forecast_fr.items():
            layout.addWidget(fr)

        # Set the height of the scroll area
        item_height = layout.itemAt(0).widget().height()

        print(item_height)
        
        # Connect the scroll buttons to the scroll functions
        self.nexth.clicked.connect(lambda: self.qsmove_right(self.hourly_scrollArea, item_height))
        self.previoush.clicked.connect(lambda: self.qsmove_left(self.hourly_scrollArea, item_height))

    def qsmove_left(self, scr, item_height):
        scr.horizontalScrollBar().setValue(scr.horizontalScrollBar().value() - item_height)

    def qsmove_right(self, scr, item_height):
        scr.horizontalScrollBar().setValue(scr.horizontalScrollBar().value() + item_height) 

    def daily_forecast_scr(self):
        daily_forecast_but = self.translator.parse_daily_forecast()

        for but_date, but in daily_forecast_but.items():
            but.clicked.connect(
                lambda _, but_date=but_date: self.on_daily_forecast_button_clicked(but_date))

        layout = self.daily_scrollAreaCont.layout()
        if layout is not None:
            QWidget().setLayout(layout)

        layout = QHBoxLayout(self.daily_scrollAreaCont)
        for but_date, but in daily_forecast_but.items():
            layout.addWidget(but)

        self.nextd.clicked.connect(
            lambda: self.qsmove_right(self.daily_scrollArea))
        self.previousd.clicked.connect(
            lambda: self.qsmove_left(self.daily_scrollArea))

    def display_location(self, coordinates: tuple[float, float]) -> None:
        weatherData = WeatherData(coordinates, 'ru')
        self.translator = Translate(weatherData)
        if isinstance(weatherData.data, str):
            raise ValueError()

        for name, value in self.translator.get_current_translation().items():
            if value is not None:
                widget = getattr(self, name)
                widget.setText(str(value))

        self.daily_forecast_scr()

    def set_bottom_right(self) -> None:
        desktop = QApplication.primaryScreen().geometry()
        app_size = self.size()
        screen_without_toolbar_size = QApplication.primaryScreen().availableGeometry()
        self.move(desktop.width() - app_size.width(),
                  (desktop.height() - app_size.height()) - (desktop.height() - screen_without_toolbar_size.height()))

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
