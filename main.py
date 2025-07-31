import os
import shutil

working_dir = input("Enter the full path of the folder you want to organize: ").strip()

if not os.path.exists(working_dir):
    print("The folder you enter does not exist")
    exit()

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



os.chdir(files_dir)
os.makedirs(os.path.join(files_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(files_dir, "music"), exist_ok=True)
os.makedirs(os.path.join(files_dir, "documents"), exist_ok=True)
os.makedirs(os.path.join(files_dir, "scripts"), exist_ok=True)
os.makedirs(os.path.join(files_dir, "archives"), exist_ok=True)
os.makedirs(os.path.join(files_dir, "packages"), exist_ok=True)
os.makedirs(os.path.join(files_dir, "others"), exist_ok=True)

file_types = {

    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "music": [".mp3", ".wav", ".aac"],
    "documents": [".pdf", ".docx", ".txt"],
    "scripts": [".py", ".js", ".sh"],
    "archives" : [".zip", ".tar.gz", ".tar.xz"],
    "packages": [".rpm", ".deb", ".exe", ".msi"],
    "others": [".html"]
}

image_dir = os.path.join(files_dir, "images")
music_dir = os.path.join(files_dir, "music")
document_dir = os.path.join(files_dir, "documents")
script_dir = os.path.join(files_dir, "scripts")
archive_dir = os.path.join(files_dir, "archives")
package_dir = os.path.join(files_dir, "packages")
other_dir = os.path.join(files_dir, "others")

working_extension = []

for f in os.listdir(files_dir):
    filename, fileextension = os.path.splitext(f)
    for ext in file_types.items():
        for x in ext[1]:
            if fileextension == x:
                if image_dir == os.path.join(files_dir, ext[0]):
                    shutil.move(f, image_dir)
                if music_dir == os.path.join(files_dir, ext[0]):
                    shutil.move(f, music_dir)
                if document_dir == os.path.join(files_dir, ext[0]):
                    shutil.move(f, document_dir)
                if script_dir == os.path.join(files_dir, ext[0]):
                    shutil.move(f, script_dir)
                if archive_dir == os.path.join(files_dir, ext[0]):
                    shutil.move(f, archive_dir)
                if other_dir == os.path.join(files_dir, ext[0]):
                    shutil.move(f, other_dir)
                if package_dir == os.path.join(files_dir, ext[0]):
                    shutil.move(f, package_dir)


 
   
    



