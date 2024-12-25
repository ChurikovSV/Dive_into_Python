# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os


def sort_files(source_directory):
    video_ext = ['.mp4', '.avi', '.mkv']
    image_ext = ['.jpg', '.jpeg', '.png']
    text_ext = ['.txt', '.doc', '.pdf']

    for file in os.listdir(source_directory):
        if os.path.isfile(os.path.join(source_directory, file)):
            file_ext = os.path.splitext(file)[1]

            if not os.path.exists(source_directory):
                os.makedirs(source_directory)

            if file_ext in video_ext:
                destination = os.path.join(source_directory, 'videos')
            elif file_ext in image_ext:
                destination = os.path.join(source_directory, 'images')
            elif file_ext in text_ext:
                destination = os.path.join(source_directory, 'text')

            os.rename(os.path.join(source_directory, file), os.path.join(destination, file))


if __name__ == '__main__':
    source_directory = r'C:\Users\Churikov-SV\Python_Project\Dive_into_Python\Lesson_07'
    sort_files(source_directory)
