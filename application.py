import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QVBoxLayout, QWidget
from yaweather import YaWeather, cities


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setGeometry(50, 50, 300, 200)

        # Create a label to display the weather
        self.weather_label = QLabel()
        self.weather_label.setAlignment(Qt.AlignCenter)

        # Connect to the yandex weather API
        self.ywm = YaWeather(api_key='69837bd5-2216-4f9d-b4bf-1d4ff578de56')

        # Create box locate
        self.create_cb_countries()
        self.create_cb_cities()

        # Create a layout and add the widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.countries_combo)
        layout.addWidget(self.cities_combo)
        layout.addWidget(self.weather_label)
        self.setLayout(layout)

    def country_changed(self):
        country = self.countries_combo.currentText()
        self.weather_label.setText(country)
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
        self.update_weather(coordinates)

    def update_weather(self, coordinates):
        res = self.ywm.forecast(coordinates)
        weather_string = f'Now: {res.fact.temp} °C, feels like {res.fact.feels_like} °C'
        self.weather_label.setText(weather_string)

    def create_cb_countries(self):
        self.countries_combo = QComboBox()
        countries = [c.name() for c in cities.CountryBase.__subclasses__()]
        countries.sort()
        self.countries_combo.addItems(countries)
        self.countries_combo.currentIndexChanged.connect(self.country_changed)

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
    sys.exit(app.exec_())
