import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):    
    abs_working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_filepath.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
    if not os.path.isfile(abs_filepath):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_filepath, "r") as f:
            content = f.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += '[...File "{file_path}" truncated at 10000 characters]'        
        return content
    
    except Exception as e:
        return f'Error reading file "{file_path}": {e}' 
