import sys

# my files
from location import Location
from translate import Translate
from weatherDataWAPI import WeatherData
import path.res
from path.interface import Ui_MainWindow
# pyqt6
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtCore import Qt, QEvent, QResource
from PyQt6.QtWidgets import QSystemTrayIcon, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton
from PyQt6.QtGui import QIcon, QAction, QGuiApplication


class createGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.initGUI()
        
        self._init_(None)

        self.display_location(text=None)
        self.on_daily_forecast_button_clicked(
            list(self.daily_forecast_but.keys())[0])

    def _init_(self, text):
        self.weatherData = WeatherData('ru', text)
        self.translator = Translate(self.weatherData)

        if isinstance(self.weatherData.data, str):
            print("беда")

    def initGUI(self):
        # window options
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.set_bottom_right()

        # minimazed and close buttons
        self.closeBtn.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.hideBtn.clicked.connect(self.toggle_tray)

        # tray
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(
            QtWidgets.QStyle.StandardPixmap.SP_DialogApplyButton))
        self.tray_icon.activated.connect(self.toggle_tray)

        # searching
        self.clear.clicked.connect(lambda: self.searchEdit.clear())
        self.search.clicked.connect(lambda: self.display_location(self.searchEdit.toPlainText().strip())
                                    if self.searchEdit.toPlainText().strip() else self.text.setText("Empty"))
        self.search_location.clicked.connect(
            lambda: self.display_location(text=None))

    def on_daily_forecast_button_clicked(self, date_str):
        hourly_forecast_fr = self.translator.parse_hourly_forecast(date_str)

        layout = self.hourly_scrollAreaCont.layout()
        if layout is not None:
            QWidget().setLayout(layout)

        layout = QHBoxLayout(self.hourly_scrollAreaCont)
        for fr_date, fr in hourly_forecast_fr.items():
            layout.addWidget(fr)

    def daily_forecast_scr(self):
        self.daily_forecast_but = self.translator.parse_daily_forecast()

        self.prognoz14.setText(
            f'Прогноз на {len(self.daily_forecast_but.keys())} дней')

        for but_date, but in self.daily_forecast_but.items():
            but.clicked.connect(
                lambda _, but_date=but_date: self.on_daily_forecast_button_clicked(but_date))

        layout = self.daily_scrollAreaCont.layout()
        if layout is not None:
            QWidget().setLayout(layout)

        layout = QHBoxLayout(self.daily_scrollAreaCont)
        for but_date, but in self.daily_forecast_but.items():
            layout.addWidget(but)

    def display_location(self, text: str) -> None:
        self._init_(text)

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
