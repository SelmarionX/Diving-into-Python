import os
import logging
from collections import namedtuple


def gather_directory_info(directory_path):
    logging.basicConfig(filename='directory_info.log', level=logging.INFO)
    FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

    if not os.path.isdir(directory_path):
        logging.error("Ошибка! Неверно указан путь")
        return

    file_info_list = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        name, extension = os.path.splitext(item)
        is_directory = os.path.isdir(item_path)
        parent_directory = os.path.basename(directory_path)
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        file_info_list.append(file_info)
        logging.info(
            f"Имя файла без расширения или название каталога: {item_path},\n"
            f"Расширение, если это файл: {extension},\n"
            f"Флаг каталога: {is_directory},\n"
            f"Название родительского каталога: {parent_directory}")

    with open('directory_info.txt', 'w') as file:
        for file_info in file_info_list:
            file.write(
                f"Имя файла без расширения или название каталога: {file_info.name},\n"
                f"Расширение, если это файл: {file_info.extension},\n"
                f"Флаг каталога: {file_info.is_directory},\n"
                f"Название родительского каталога: {file_info.parent_directory}\n")


if __name__ == "__main__":
    import sys

    print(gather_directory_info(r'C:\Users\Alexander\Desktop\hw15'))
