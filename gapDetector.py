import os
import re

def close_gaps(folder, prefix, extension):
    # Pattern to match files like prefixNNN.extension, e.g. spam001.txt
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+){re.escape(extension)}$")
    
    files = []
    for f in os.listdir(folder):
        match = pattern.match(f)
        if match:
            number = int(match.group(1))
            files.append((number, f))
    
    # Sort files by their number
    files.sort(key=lambda x: x[0])
    
    expected_num = 1
    for actual_num, filename in files:
        if actual_num != expected_num:
            old_path = os.path.join(folder, filename)
            new_name = f"{prefix}{expected_num:03d}{extension}"
            new_path = os.path.join(folder, new_name)
            print(f"Renaming {filename} -> {new_name}")
            os.rename(old_path, new_path)
        expected_num += 1

folder_path = input("Enter folder path: ").strip()
prefix = input("Enter file prefix (e.g., spam): ").strip()
extension = input("Enter file extension (e.g., .txt): ").strip()
close_gaps(folder_path, prefix, extension)
