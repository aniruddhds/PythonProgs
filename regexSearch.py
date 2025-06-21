import os
import re

def searchText(folder_path, regex_pattern):
    pattern = re.compile(regex_pattern)

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_num, line in enumerate(file, start=1):
                        if pattern.search(line):
                            print(f"{filename} (line {line_num}): {line.strip()}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")


folder = input("Enter the folder path containing .txt files: ").strip()
regex = input("Enter the regular expression to search for: ").strip()
searchText(folder, regex)