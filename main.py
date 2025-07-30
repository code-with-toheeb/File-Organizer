import os
import shutil

working_dir = "/home/hashotocodes/Downloads"
os.chdir(working_dir)
os.makedirs(os.path.join(working_dir, "files"), exist_ok=True)
os.makedirs(os.path.join(working_dir, "directories"), exist_ok=True)

#print(os.listdir(working_dir))
files_dir = os.path.join(working_dir, "files")
directories_dir = os.path.join(working_dir, "directories")

for file in os.listdir(working_dir):
    
    item_path = os.path.join(working_dir, file)

    if file in ["files", "directories"]:
        continue

    if os.path.isfile(item_path):
        shutil.move(item_path, files_dir)
    if os.path.isdir(item_path):
        shutil.move(item_path, directories_dir)

