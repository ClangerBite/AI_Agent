import os

def get_files_info(working_directory, directory=None):
    
    abs_working_dir = os.path.abspath(working_directory)
    
    if directory:
        abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))
    else:
        abs_target_dir = abs_working_dir
    
    if not os.path.isdir(abs_target_dir):
        return f'Error: "{directory}" is not a directory'
    
    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    try:
        return "\n".join(list(map(lambda i: build_line(abs_target_dir,i), os.listdir(abs_target_dir))))
    except Exception as e:
        return f"Error listing files: {e}"
    
    
def build_line(directory, item):
    filepath = os.path.join(directory, item)    
    return f'- {item}: file_size = {os.path.getsize(filepath)} bytes, is_dir={os.path.isdir(filepath)}'  