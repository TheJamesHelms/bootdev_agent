import os
import io
import config

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs,file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs,target_file_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            with open(target_file_path, "r") as f:
                content = f.read(config.MAX_CHARS)
                # After reading the first MAX_CHARS...
                if f.read(1):
                    content += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'

        return content
    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns the contents of a file as a text string. The length of the content will be truncated to MAX_CHARS if the content string exceeds MAX_CHARS.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to retrieve contents from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
