# Recursive Counter

Recursive Counter is a powerful Python program designed to recursively count the number of lines in each file within a specified folder and its subfolders.

## Getting Started

### Installation

To get started, you can conveniently install the executable file from our [GitHub releases page](https://github.com/Ryan-Rudd/Recursive-Counter/releases).

1. Download the `.exe` file and save it to your desired location.
2. Copy the folder path where the executable file is located.

### Setting up the Environment

1. Navigate to the Windows icon and click on "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables" button.
3. Under "System Variables", locate the "Path" variable and click on the "Edit" button.
4. Click the "New" button and paste the folder path where the executable file is located.
5. Close all currently opened terminal or command prompt windows and reopen them.
6. Type "counter" in your command line to run the program.

## Code Overview

The program consists of two main functions:

- `count_lines_in_file(file_path)`: This function takes the path to a file as an argument and returns the number of lines in the file. If there is an IOError or UnicodeDecodeError, it returns 0.
- `count_lines_in_folder(folder_path)`: This function takes the path to a folder as an argument. It walks through the folder and its subfolders, counting the total number of lines in all files. It also tracks the total number of files and identifies the file with the largest number of lines.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License.
