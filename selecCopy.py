import os
import shutil

def copyFilesExt(src_folder, dst_folder, extension):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(extension.lower()):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_folder, file)

                if os.path.exists(dst_file):
                    base, exten = os.path.splitext(file)
                    count = 1
                    while os.path.exists(dst_file):
                        dst_file = os.path.join(dst_folder, f"{base}_{count}{exten}")
                        count += 1

                shutil.copy2(src_file, dst_file)
                print(f"Copied: {src_file} -> {dst_file}")

source = input("Enter the source folder path: ").strip()
destination = input("Enter the destination folder path: ").strip()
exten = input("Enter the file extension to search for (e.g., .pdf, .jpg): ").strip()    
copyFilesExt(source, destination, exten)