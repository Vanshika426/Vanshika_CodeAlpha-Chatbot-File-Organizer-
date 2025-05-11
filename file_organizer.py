import os
import shutil

# Step 1: Folder ka path do (jaise Downloads)
source_folder =   r'C:\Users\localadmin\Desktop\stock portfolio tracker'


# Step 2: File types define karo
file_types = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Videos': ['.mp4', '.mov'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Music': ['.mp3'],
    'Archives': ['.zip', '.rar'],
    'Others': []
}

# Step 3: Organize function
def organize_files():
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(file.endswith(ext) for ext in extensions):
                    dest_folder = os.path.join(source_folder, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    break
            if not moved:
                dest_folder = os.path.join(source_folder, 'Others')
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file))

if __name__ == "__main__":
    organize_files()
    print("Files organized successfully!")