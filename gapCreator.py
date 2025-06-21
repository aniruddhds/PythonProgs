import os
import re

def insert_gaps(folder, prefix, extension, start_num, gap_size=1):
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+){re.escape(extension)}$")
    
    files = []
    for f in os.listdir(folder):
        match = pattern.match(f)
        if match:
            number = int(match.group(1))
            if number >= start_num:
                files.append((number, f))
    
    # Sort descending to avoid overwriting when renaming
    files.sort(key=lambda x: x[0], reverse=True)
    
    for number, filename in files:
        old_path = os.path.join(folder, filename)
        new_number = number + gap_size
        new_name = f"{prefix}{new_number:03d}{extension}"
        new_path = os.path.join(folder, new_name)
        print(f"Renaming {filename} -> {new_name}")
        os.rename(old_path, new_path)

folder_path = input("Enter folder path: ").strip()
prefix = input("Enter file prefix (e.g., spam): ").strip()
extension = input("Enter file extension (e.g., .txt): ").strip()
start_num = int(input("Enter the starting number to insert gap at: ").strip())
gap_size = int(input("Enter gap size (default 1): ").strip() or "1")
insert_gaps(folder_path, prefix, extension, start_num, gap_size)
