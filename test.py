from PIL import Image, ImageOps
import os

# указываем путь к папке с изображениями
img_dir = 'C:/Users/udinc/OneDrive/Рабочий стол/проект/Weather/path/icons'

# создаем новую папку для сохранения измененных изображений
new_dir = 'C:/Users/udinc/OneDrive/Рабочий стол/проект/Weather/path/icons/ma'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

# перебираем все файлы в папке
for filename in os.listdir(img_dir):
    # проверяем, является ли файл изображением
    if filename.endswith('.png'):
        # открываем изображение
        img = Image.open(os.path.join(img_dir, filename))
        
        # изменяем цвет изображения на черно-белый
        if img.mode == 'P' and 'transparency' in img.info:
            img = img.convert('RGBA')
            
        img = ImageOps.invert(img.convert('RGB'))
        
        # добавляем постфикс в имя файла
        new_filename = os.path.splitext(filename)[0] + '_inv' + os.path.splitext(filename)[1]
        
        # сохраняем измененное изображение в новую папку
        img.save(os.path.join(new_dir, new_filename))