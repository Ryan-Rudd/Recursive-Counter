import os

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
            return line_count
    except (IOError, UnicodeDecodeError):
        return 0

def count_lines_in_folder(folder_path):
    total_lines = 0
    file_count = 0
    largest_file = ('', 0)
    total_size = 0
    total_characters = 0
    total_characters_without_spaces = 0
    total_words = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            line_count = count_lines_in_file(file_path)
            total_lines += line_count
            file_count += 1
            file_size = os.path.getsize(file_path)
            total_size += file_size
            total_characters += count_characters(file_path)
            total_characters_without_spaces += count_characters_without_spaces(file_path)
            total_words += count_words(file_path)
            # Check if current file has more lines than the largest file
            if line_count > largest_file[1]:
                largest_file = (file_path, line_count)

    print(f"\nTotal files: {file_count}")
    print(f"Total lines: {total_lines}")
    print(f"Total size: {total_size} bytes")
    print(f"Total characters: {total_characters}")
    print(f"Total characters (without spaces): {total_characters_without_spaces}")
    print(f"Total words: {total_words}")
    if largest_file[0]:
        print(f"Largest file: {largest_file[0]} ({largest_file[1]} lines)")

def count_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return len(content)
    except (IOError, UnicodeDecodeError):
        return 0

def count_characters_without_spaces(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            content = content.replace(' ', '')  # Remove spaces
            return len(content)
    except (IOError, UnicodeDecodeError):
        return 0

def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except (IOError, UnicodeDecodeError):
        return 0

folder_path = input("Enter the folder path: ")
count_lines_in_folder(folder_path)
