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
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            line_count = count_lines_in_file(file_path)
            total_lines += line_count
            file_count += 1
            # Check if current file has more lines than the largest file
            if line_count > largest_file[1]:
                largest_file = (file_path, line_count)

    print(f"\nTotal files: {file_count}")
    print(f"Total lines: {total_lines}")
    if largest_file[0]:
        print(f"Largest file: {largest_file[0]} ({largest_file[1]} lines)")

folder_path = input("Enter the folder path: ")
count_lines_in_folder(folder_path)
