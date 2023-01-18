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
        
        # combo box country and city
        self.countries.addItems(Location.get_countries())
        self.countries.currentIndexChanged.connect(self.populate_cities)
        
        # info weather
        self.all_info()
    
    def all_info(self):
        temperature = Location.temperature
        feel_temperature = Location.feel_temperature
        humidity = Location.humidity
        cloudness = Location.cloudness
        condition = Location.condition

        weather = (f'''Now: {temperature} °C,
                    feels like {feel_temperature} °C, 
                    humidity: {humidity}, 
                    cloudness: {cloudness}, 
                    condition: {condition}''')
        
        self.Text.setText(weather)
    
    def populate_cities(self):
        country = self.countries.currentText()
        self.cities.clear()
        self.cities.addItems(Location.get_cities(country))
    
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