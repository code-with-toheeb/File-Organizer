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

file_types = {

    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "music": [".mp3", ".wav", ".aac"],
    "documents": [".pdf", ".docx", ".txt"],
    "scripts": [".py", ".js", ".sh", ".php"],
    "archives" : [".zip", ".tar.gz", ".tar.xz", ".xz", ".gz"],
    "packages": [".rpm", ".deb", ".exe", ".msi"],
    "others": []
}

for category in file_types:
    os.makedirs(os.path.join(files_dir, category), exist_ok=True)

for f in list(os.listdir(files_dir)):
    path = os.path.join(files_dir, f)
    
    if os.path.isfile(path):
        _,ext = os.path.splitext(f)
        moved = False

        for category, extensions in file_types.items():
            if ext.lower() in extensions:
                dest_folder = os.path.join(files_dir, category)
                dest_path = os.path.join(dest_folder, f)

                if os.path.exists(dest_path):
                    base, extension = os.path.splitext(f)
                    counter = 1

                    while os.path.exists(dest_path):
                        new_name = f"{base}_{counter}{extension}"
                        dest_path = os.path.join(dest_folder, new_name)
                        counter += 1

                shutil.move(path, dest_path)
                moved = True
                break
            
        if not moved:
            dest_folder = os.path.join(files_dir, "others")
            dest_path = os.path.join(dest_folder, f)

            if os.path.exists(dest_path):
                base, extension = os.path.splitext(f)
                counter = 1
                                    
                while os.path.exists(dest_path):
                    new_name = f"{base}_{counter}{extension}"
                    dest_path = os.path.join(dest_folder, new_name)
                    counter +=1
            shutil.move(path, dest_path)
                

print("File Organized Successfully")



