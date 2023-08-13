import os
import shutil
import re
import sys
from pathlib import Path


CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
 

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].lower()

def normalize(name: str) -> str:
    ext = get_extension(name)
    name_without_extension = os.path.splitext(os.path.basename(name))[0]
    # print(name_without_extension)  
    t_name = name_without_extension.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    t_name = t_name + "." + ext
    return t_name

# Функція для сортування папки
def sort_folder(folder_path):
    image_extensions = ('JPEG', 'PNG', 'JPG', 'SVG')
    video_extensions = ('AVI', 'MP4', 'MOV', 'MKV')
    document_extensions = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    audio_extensions = ('MP3', 'OGG', 'WAV', 'AMR')
    archive_extensions = ('ZIP', 'GZ', 'TAR')

    known_extensions = set()
    unknown_extensions = set()
    
    images_files   = []
    video_files    = []
    documents_file = []
    audio_files    = []
    archive_files  = []
    unknown_files  = []
    
    
    

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            extension = os.path.splitext(file)[1][1:].upper()
            if extension in image_extensions:
                images_files.append(os.path.basename(file))
                move_file(file, root, 'images')
                known_extensions.add(extension)   
            elif extension in video_extensions:
                video_files.append(os.path.basename(file))
                move_file(file, root, 'videos')
                known_extensions.add(extension)
            elif extension in document_extensions:
                documents_file.append(os.path.basename(file))
                move_file(file, root, 'documents')
                known_extensions.add(extension)
            elif extension in audio_extensions:
                audio_files.append(os.path.basename(file))
                move_file(file, root, 'audio')
                known_extensions.add(extension)
            elif extension in archive_extensions:
                archive_files.append(os.path.basename(file))
                unpack_archive(file, root, 'archives')
                known_extensions.add(extension)
            else:
                unknown_files.append(os.path.basename(file))
                move_file(file, root, 'unknown')
                unknown_extensions.add(extension)

    return known_extensions, unknown_extensions, images_files, video_files, documents_file, audio_files, archive_files, unknown_files

# Функція для переміщення файлу в нову папку
def move_file(file, source_folder, destination_folder):
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, file)
    destination_path = os.path.join(destination_folder, normalize(file))
    os.makedirs(destination_folder, exist_ok=True)
    shutil.move(source_path, destination_path)

# Функція для розпакування архіву та переміщення вмісту до нової папки
def unpack_archive(file, source_folder, destination_folder):
    archive_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, normalize(file))
    os.makedirs(destination_path, exist_ok=True)
    shutil.unpack_archive(archive_path, destination_path)
    # Перенесення вмісту архіву до папки archives
    for root, dirs, files in os.walk(destination_path):
        for file in files:
            move_file(file, root, destination_folder)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python sort.py <folder_path>')
        sys.exit(1)

    folder_path = sys.argv[1]
    known_extensions, unknown_extensions, images_files, video_files, documents_file, audio_files, archive_files, unknown_files = sort_folder(folder_path)

    print('Known extensions:')
    print(known_extensions)
    print('Unknown extensions:')
    print(unknown_extensions)
    print('images files:')
    print(images_files)
    print('video files:')
    print(video_files)
    print('documents file:')
    print(documents_file)
    print('audio files:')
    print(audio_files)
    print('unknown files:')
    print(unknown_files)
    
    
