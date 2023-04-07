from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)

# Создаем QScrollArea и задаем его свойства
scrollArea = QScrollArea()
scrollArea.setWidgetResizable(True)
scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

# Создаем QWidget, который будет являться содержимым QScrollArea
widget = QWidget()
layout = QVBoxLayout(widget)

# Создаем элементы, которые будут добавлены в QWidget
for i in range(50):
    label = QLabel("Label " + str(i))
    layout.addWidget(label)

# Добавляем QWidget в QScrollArea
scrollArea.setWidget(widget)

# Устанавливаем размер шага прокрутки равным размеру одного элемента
scrollbar = scrollArea.verticalScrollBar()
item_height = layout.itemAt(0).widget().height()
scrollbar.setSingleStep(item_height)

# Функции-обработчики нажатия клавиш
def scroll_up():
    scrollbar.setValue(scrollbar.value() - item_height)

def scroll_down():
    scrollbar.setValue(scrollbar.value() + item_height)

# Подключаем слоты к сигналу нажатия клавиши
scrollArea.keyPressEvent = lambda event: scroll_down() if event.key() == Qt.Key_Down else (scroll_up() if event.key() == Qt.Key_Up else None)

# Показываем QScrollArea
scrollArea.show()

sys.exit(app.exec_())