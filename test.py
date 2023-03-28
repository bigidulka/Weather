from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QLabel, QPushButton
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QScrollArea and add a widget to it
        scroll_area = QScrollArea(parent=self)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.addWidget(QLabel('This is a label inside the scroll area'))
        scroll_area.setWidget(scroll_widget)

        # Create a button and set its parent widget
        button = QPushButton('Click me', parent=self)

        # Create a QHBoxLayout and add the QScrollArea and the button to it
        main_layout = QHBoxLayout()
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(button)

        # Set the main layout for the widget
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
