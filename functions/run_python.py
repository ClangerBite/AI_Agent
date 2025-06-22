import os
import subprocess


def run_python_file(working_directory, file_path):
        
    abs_working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_filepath.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
    if not os.path.exists(abs_filepath):        
        return f'Error: File "{file_path}" not found.'
    
    if file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(abs_filepath, timeout=30, capture_output=True)
    
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        
        if len(result.stdout) == 0:
            return 'No output produced.'    
    
        return f"STDOUT: {result.stdout} STDERR: {result.stderr}"
        
    
    except Exception as e:
        return f'Error: executing Python file: {e}'