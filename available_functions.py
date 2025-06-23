from google.genai import types

from config import MAX_CHARS

def available_functions():
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )
    
    schema_get_files_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads a file in the specified directory to a maximum of {MAX_CHARS} characters, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The location of the file to read, relative to the working directory.",
                ),
            },
        ),
    )
    
    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Executes a specified python script, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The location of the file to execute, relative to the working directory.",
                ),
                "args": types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments given after the name fo the python script. If not provided, args default to None.",
                ),
            },
        ),
    )

    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes to a specified file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The location of the file to be written to, relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to be written to the specified file.",
                ),
            },
        ),
    )
    
    
    
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_files_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )
    return available_functions