import os

def write_file(working_directory, file_path, content):
    
    
    abs_working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_filepath.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
    if not os.path.exists(abs_filepath):
        try:
            os.makedirs(os.path.dirname(abs_filepath), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    
    if os.path.exists(abs_filepath) and os.path.isdir(abs_filepath):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        with open(abs_filepath, "w") as f:
            f.write(content) 
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error writing to file "{file_path}": {e}'