

import os

def validate_file_path(file_path, extension = None) -> bool:
    if not file_path:
            print("Error: No file specified. Please provide a file path after the --file option.")       
            return False
    absolute_path = os.path.abspath(file_path) 
    if not os.path.exists(absolute_path):
            print(f"Error: The file {absolute_path} does not exist.")
            return False
    path_info = os.path.splitext(absolute_path)
    if extension and path_info[1].lower() != extension.lower():
            print(f"Error: The file {absolute_path} is not a {extension} file.")
            return False
    return True