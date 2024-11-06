import os
import logging
from collections import namedtuple
import argparse

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def collect_directory_info(directory_path):
    logging.info(f"Начинаем сбор информации из директории: {directory_path}")
    
    file_info_list = []
    
    if not os.path.isdir(directory_path):
        logging.error(f"Путь {directory_path} не является директорией или не существует!")
        return []
    
    for root, dirs, files in os.walk(directory_path):
        parent_directory = os.path.basename(root)
        logging.info(f"Собираем информацию из каталога: {root}")
        
        for filename in files:
            name, extension = os.path.splitext(filename)
            extension = extension.lstrip('.')
            file_info_list.append(FileInfo(
                name=name,
                extension=extension,
                is_directory=False,
                parent_directory=parent_directory
            ))
            logging.info(f"Найден файл: {filename} (расширение: {extension})")
        
        for dirname in dirs:
            file_info_list.append(FileInfo(
                name=dirname,
                extension='',
                is_directory=True,
                parent_directory=parent_directory
            ))
            logging.info(f"Найден каталог: {dirname}")
    
    return file_info_list

def setup_logging():
    logging.basicConfig(
        filename='directory_info.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Логирование настроено.")

def main():
    parser = argparse.ArgumentParser(description="Собрать информацию о содержимом директории.")
    parser.add_argument('directory', type=str, help="Путь к директории для сбора информации")
    args = parser.parse_args()
    
    setup_logging()
    
    file_info_list = collect_directory_info(args.directory)
    
    for file_info in file_info_list:
        print(file_info)
    
    with open('directory_info.txt', 'w') as f:
        for file_info in file_info_list:
            f.write(f"Name: {file_info.name}, Extension: {file_info.extension}, "
                    f"Is Directory: {file_info.is_directory}, Parent Directory: {file_info.parent_directory}\n")

if __name__ == '__main__':
    main()
