import sys

# my files
import interface
from location import Location
from weatherdata import WeatherData

# pyqt6
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import QSystemTrayIcon, QApplication, QWidget
from PyQt6.QtGui import QIcon, QAction, QGuiApplication

class createGUI(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.initGUI()

    def initGUI(self):
        # window options
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.set_bottom_right()
        self.setFixedSize(600, 605)

        # minimazed and close buttons
        self.close_button.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.hide_button.clicked.connect(self.to_tray)
        
        # tray
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogApplyButton))
        self.tray_icon.activated.connect(self.from_tray)
        
        # info weather
        # self.cities.currentIndexChanged.connect(self.all_info)
    
        # combo box country and city
        self.countries.addItems(Location.get_countries())
        self.countries.currentIndexChanged.connect(self.country_changed)
        
        self.cities.setEnabled(False)

    def city_changed(self):
        city = self.cities.currentText()
        if not city:
            return
        self.all_info()
    
    def country_changed(self):
        country = self.countries.currentText()
        if not country:
            return
        self.cities.setEnabled(True)
        self.populate_cities(country)
        self.cities.currentIndexChanged.connect(self.city_changed)
    
    def populate_cities(self, country):
        self.cities.clear()
        self.cities.addItems(Location.get_cities(country))
        
    def all_info(self):
        country = self.countries.currentText()
        city = self.cities.currentText()
        
        self.weather_data = WeatherData(country, city)

        temperature = self.weather_data.temperature
        feel_temperature = self.weather_data.feel_temperature
        humidity = self.weather_data.humidity
        cloudness = self.weather_data.cloudness
        condition = self.weather_data.condition

        weather = f'''Now: {temperature} °C,\nfeels like {feel_temperature} °C,\nhumidity: {humidity},\ncloudness: {cloudness},\ncondition: {condition}'''
        
        self.Text.setText(weather)
    
    def set_bottom_right(self):
        screen_size = QApplication.primaryScreen().geometry()
        app_size = QWidget.size(self)
        screen_without_toolbar_size = QApplication.primaryScreen().availableGeometry()
        self.move(screen_size.width()-app_size.width(),
                  (screen_size.height() - app_size.height()) - (screen_size.height() - screen_without_toolbar_size.height()))
    
    def to_tray(self):
        self.setVisible(False)
        self.tray_icon.show()

    def from_tray(self):
        self.setVisible(True)
        self.tray_icon.hide()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = createGUI()
    window.show()
    app.exec()