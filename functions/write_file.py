import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if os.path.commonpath([abs_working_dir]) != os.path.commonpath([abs_working_dir, abs_file_path]):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 
    
    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.exists(parent_dir):
        try:
            os.makedirs(parent_dir)
        
        except Exception as e:
            return f"could not create parent dir: {parent_dir} = {e}"
    
    try:
        with open(abs_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Failed to write to file: {file_path}, {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or writes to a new file if it doesn't exists (and creates required parent dirs safely), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to write to the file as a string.",
            ),
        },
    ),
)