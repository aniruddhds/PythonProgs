import os

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            try:
                fp = os.path.join(root, f)
                total_size += os.path.getsize(fp)
            except OSError:
                pass
    return total_size

def findFiles(root_dir, size_threshold=100*1024*1024):
    print(f"Files larger than {size_threshold / (1024*1024)} MB:")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(file_path)
                if size > size_threshold:
                    print(f"File: {os.path.abspath(file_path)} - Size: {size / (1024*1024):.2f} MB")
            except OSError:
                pass

    print(f"\nFolders larger than {size_threshold / (1024*1024)} MB:")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        try:
            folder_size = get_folder_size(dirpath)
            if folder_size > size_threshold:
                print(f"Folder: {os.path.abspath(dirpath)} - Size: {folder_size / (1024*1024):.2f} MB")
        except OSError:
            pass

directory = input("Enter the root directory to search: ").strip()
findFiles(directory)