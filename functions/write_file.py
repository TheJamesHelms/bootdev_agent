import os
import io

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs,file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs,target_file_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            parent_dir = os.path.dirname(target_file_path)
            if not os.path.isdir(parent_dir):
                os.makedirs(parent_dir, exist_ok=True)
            with open(target_file_path,"w") as w:
                w.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")

schemma_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Runs the python located at the file path provided and passing in the arguments from args",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the file to write, relative to the working directory (default is the working directory itself)",
                },
                "content":{
                    "type": "string",
                    "description": "String to write to file"
                },
            },
        },
    },
}
