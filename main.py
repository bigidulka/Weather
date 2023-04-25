import sys

# my files
from location import Location
from translate import Translate
from weatherDataWAPI import WeatherData
import path.res
from path.interface import Ui_MainWindow
# pyqt6
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtCore import Qt, QEvent, QResource, QTimer
from PyQt6.QtWidgets import QSystemTrayIcon, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton, QToolTip, QMessageBox, QFrame, QLabel
from PyQt6.QtGui import QIcon, QAction, QGuiApplication, QPixmap


class WeatherApp(QtWidgets.QMainWindow, Ui_MainWindow):
    LANGUAGE = 'ru'

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.initGUI()

        self._init_(None)

    def _init_(self, text):
        coordinates = Location.get_coor_city(text)

        self.translation = Translate.translation_from_the_front(
            WeatherApp.LANGUAGE)

        if text and not coordinates:
            self.error_output(f"'{text}': {self.translation['not_found']}")
        else:
            try:
                self.weatherData = WeatherData(WeatherApp.LANGUAGE, coordinates)
                self.translator = Translate(self.weatherData)
                for name, value in self.translator.get_current_translation().items():
                    widget = getattr(self, name)
                    widget.setText(str(value)) if value else None
                self.daily_forecast_scr()
                self.on_daily_forecast_button_clicked(list(self.daily_forecast_but.keys())[0])

                icon = QPixmap(self.weatherData.data['current']['condition']['icon'].replace('//cdn.weatherapi.com', 'path').replace('\\', '/'))
                self.ico.setPixmap(icon.scaled(100, 100))
                
                self.searchEdit.setPlaceholderText(self.translation['search_placeholder'])

            except Exception as e:
                print(e)
                self.error_output(str(e))
    
    def initGUI(self):
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.set_bottom_right()

        self.closeBtn.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.hideBtn.clicked.connect(self.toggle_tray)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogApplyButton))
        self.tray_icon.activated.connect(self.toggle_tray)

        self.clear.clicked.connect(lambda: self.searchEdit.clear())
        self.search.clicked.connect(lambda: self.searh_result())
        self.search_location.clicked.connect(lambda: self._init_(None))

    def searh_result(self):
        if self.searchEdit.text().strip():
            self._init_(self.searchEdit.text().strip())
        else:
            self.error_output(self.translation['search_empty'])

    def error_output(self, text):
        timer = QTimer(self)    
        def set_error_style():
            self.title.setStyleSheet("#title { background-color: rgba(255, 0, 0, 0.4); border-radius: 0px; }")
            self.error.setText(text)
            def reset_style():
                self.title.setStyleSheet("#title { background-color: transparent; }")
                self.error.setText("")
                timer.stop()
            timer.timeout.connect(reset_style)
            timer.start(2000)
        set_error_style()

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

        for but_date, but in self.daily_forecast_but.items():
            but.clicked.connect(
                lambda _, but_date=but_date: self.on_daily_forecast_button_clicked(but_date))

        layout = self.daily_scrollAreaCont.layout()
        if layout is not None:
            QWidget().setLayout(layout)

        layout = QHBoxLayout(self.daily_scrollAreaCont)
        for but_date, but in self.daily_forecast_but.items():
            layout.addWidget(but)

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
    window = WeatherApp()
    window.show()
    app.exec()
