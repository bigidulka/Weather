import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QCursor, QIcon
from PyQt6.QtWidgets import QApplication, QComboBox, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QSystemTrayIcon
from yaweather import cities
from weatherdata import WeatherData

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # geometry app
        self.setGeometry(50, 50, 300, 200)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        # Create a label to display the weather
        self.weather_label = QLabel()
        self.weather_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a layout
        self.top_layout = QHBoxLayout()
        self.top_layout.addStretch()

        # Create box locate
        self.create_cb_countries()
        self.create_cb_cities()
        # create buttons 
        self.create_control_buttons()
        
        # Add the buttons layout to the main layout
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(self.top_layout)
        main_layout.addWidget(self.weather_label)
        main_layout.addWidget(self.countries_combo)
        main_layout.addWidget(self.cities_combo)

    def display_weather(self):
        temperature = self.weather_data.temperature
        feel_temperature = self.weather_data.feel_temperature
        humidity = self.weather_data.humidity
        cloudness = self.weather_data.cloudness
        condition = self.weather_data.condition

        weather = (f'''Now: {temperature} °C,
                    feels like {feel_temperature} °C, 
                    humidity: {humidity}, 
                    cloudness: {cloudness}, 
                    condition: {condition}''')
        
        self.weather_label.setText(weather)

    def country_changed(self):
        country = self.countries_combo.currentText()
        if not country:
            return
        self.cities_combo.setEnabled(True)
        country_class = getattr(cities, country)
        self.populate_cities_combo(country_class)

    def city_changed(self):
        city = self.cities_combo.currentText()
        if not city:
            return
        country = self.countries_combo.currentText()
        country_class = getattr(cities, country)
        coordinates = country_class.cities()[city]
        self.weather_data = WeatherData(coordinates)
        self.display_weather()

    def create_control_buttons(self):
        # Create close and minimize buttons
        close_button = QPushButton("x")
        close_button.setFixedSize(30, 30)
        close_button.setAutoFillBackground(False)
        close_button.clicked.connect(QApplication.instance().quit)

        minimize_button = QPushButton("-")
        minimize_button.setFixedSize(30, 30)
        minimize_button.setAutoFillBackground(False)
        minimize_button.clicked.connect(self.showMinimized)

        # Create a horizontal layout for the buttons
        self.top_layout.addWidget(minimize_button)
        self.top_layout.addWidget(close_button)
        self.top_layout.setContentsMargins(0, 0, 0, 0) # set the value of the margins

    def create_cb_countries(self):
        self.countries_combo = QComboBox()
        countries = [c.name() for c in cities.CountryBase.__subclasses__()]
        countries.sort()
        self.countries_combo.addItems(countries)
        self.countries_combo.currentIndexChanged.connect(self.country_changed)
        self.countries_combo.setCurrentIndex(-1)

    def create_cb_cities(self):
        self.cities_combo = QComboBox()
        self.cities_combo.setEnabled(False)
        self.cities_combo.currentIndexChanged.connect(self.city_changed)

    def populate_cities_combo(self, country_class):
        self.cities_combo.clear()
        cities_ = country_class.cities()
        cities_ = dict(sorted(cities_.items()))
        self.cities_combo.addItems(cities_.keys())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec())