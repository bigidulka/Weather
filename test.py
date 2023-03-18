from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QPainter, QPalette, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QPushButton, QLabel


class RoundedFrame(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Raised)
        self.setLineWidth(2)
        self.setMidLineWidth(0)
        self.setContentsMargins(10, 10, 10, 10)
        self.setFixedWidth(200)
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(pal)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRoundedRect(self.rect(), 10, 10)


class Swiper(QWidget):
    def __init__(self, num_frames):
        super().__init__()
        
        # Создание виджета-контейнера для содержимого
        self.widget = QWidget()
        self.widget.setLayout(QHBoxLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)

        # Создаем список фреймов и добавляем их на виджет
        self.frames = []
        for i in range(num_frames):
            frame = QFrame(self)
            frame.setObjectName('Frame')
            frame.setFixedSize(100, 100)
            frame.move(i * (frame.width() + 10) + 10, 10)

            # Создаем дочерний QLabel для отображения цифры
            label = QLabel(str(i + 1), frame)
            label.setAlignment(Qt.AlignCenter)
            label.resize(frame.size())

            self.frames.append(frame)
        
        # Отображаем первый фрейм
        self.current_frame_index = 0
        self.show_current_frame()

        # Создание кнопок назад и вперед
        self.prev_button = QPushButton()
        self.prev_button.setIconSize(QSize(30, 30))
        self.prev_button.setFixedSize(QSize(40, 40))
        self.prev_button.setIcon(QIcon('path/icons/png-transparent-arrow-double-right-arrows-icon-thumbnail.png'))
        self.prev_button.clicked.connect(self.prev)

        self.next_button = QPushButton()
        self.next_button.setIconSize(QSize(30, 30))
        self.next_button.setFixedSize(QSize(40, 40))
        self.next_button.setIcon(QIcon('path/icons/png-transparent-arrow-double-right-arrows-icon-thumbnail.png'))
        self.next_button.clicked.connect(self.next)

        # Создание горизонтального layout и добавление кнопок и виджета-контейнера
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.addWidget(self.prev_button)
        self.layout.addWidget(self.widget)
        self.layout.addWidget(self.next_button)

        # Установка текущего индекса фрейма
        self.current_frame_index = 0
        self.update_buttons()

    def show_current_frame(self):
        # Скрытие всех фреймов, кроме текущего
        for frame in self.frames:
            frame.hide()

        # Отображение текущего фрейма
        num_visible_frames = 3  # Количество отображаемых фреймов
        start_index = max(0, self.current_frame_index - num_visible_frames // 2)
        end_index = min(len(self.frames), start_index + num_visible_frames)
        for i in range(start_index, end_index):
            frame = self.frames[i]
            frame.show()
            frame.move((i - start_index) * (frame.width() + 10) + 10, 10)
    
    def prev(self):
        self.current_frame_index -= 1
        self.update_buttons()

    def next(self):
        self.current_frame_index += 1
        self.update_buttons()

    def update_buttons(self):
        # Скрытие/отображение кнопок в зависимости от текущего индекса фрейма
        self.prev_button.setVisible(self.current_frame_index > 0)
        self.next_button.setVisible(self.current_frame_index < len(self.frames) - 1)

        # Скрытие всех фреймов
        for frame in self.frames:
            frame.hide()

        # Отображение текущего фрейма
        self.frames[self.current_frame_index].show()

    def paintEvent(self, event):
        # Отрисовка фона
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Задаем круглую форму фона
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRoundedRect(self.rect(), self.height() // 2, self.height() // 2)

        # Отрисовка стрелок
        arrow_size = 20
        arrow_padding = 10
        arrow_x = (self.width() - 2 * arrow_size - arrow_padding) // 2
        arrow_y = (self.height() - arrow_size) // 2

        # Отрисовка стрелки "назад"
        if self.current_frame_index > 0:
            painter.drawPixmap(arrow_x, arrow_y, QPixmap('path/icons/png-transparent-arrow-double-right-arrows-icon-thumbnail.png').scaled(arrow_size, arrow_size, Qt.KeepAspectRatio))

        # Отрисовка стрелки "вперед"
        if self.current_frame_index < len(self.frames) - 1:
            painter.drawPixmap(self.width() - arrow_x - arrow_size, arrow_y, QPixmap('path/icons/png-transparent-arrow-double-right-arrows-icon-thumbnail.png').scaled(arrow_size, arrow_size, Qt.KeepAspectRatio))

if __name__ == '__main__':
    app = QApplication([])
    swiper = Swiper(num_frames=5)
    swiper.show()
    app.exec_()