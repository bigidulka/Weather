from PIL import Image
import os

# Укажите путь к папке, в которой находятся изображения
input_folder = 'C:/Users/udinc/OneDrive/Рабочий стол/Weather/path/fons'

# Укажите путь к папке, в которую будут сохранены измененные изображения
output_folder = 'C:/Users/udinc/OneDrive/Рабочий стол/Weather/path/fons/out'

# Укажите желаемый размер изображений (ширина, высота)
desired_size = (1024, 700)

# Цикл по всем файлам в папке ввода
for filename in os.listdir(input_folder):
    # Получаем полный путь к файлу
    input_path = os.path.join(input_folder, filename)

    # Открываем изображение с помощью библиотеки PIL
    with Image.open(input_path) as im:
        # Определяем соотношение сторон и вычисляем новый размер с сохранением пропорций
        aspect_ratio = im.width / im.height
        new_width = int(desired_size[1] * aspect_ratio)
        new_size = (new_width, desired_size[1])

        # Изменяем размер изображения
        resized_im = im.resize(new_size)

        # Сохраняем измененное изображение в папку вывода
        output_path = os.path.join(output_folder, filename)
        resized_im.save(output_path)

print("Изображения успешно изменены и сохранены в", output_folder)