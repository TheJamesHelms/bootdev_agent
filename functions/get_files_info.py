import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs,directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        if valid_target_dir:
            #print(os.listdir(target_dir))
            return_string = ""
            contents = os.listdir(target_dir)
            for item in contents:
                data = (target_dir,item)
                file_size = os.path.getsize('/'.join(data))
                is_dir = os.path.isdir('/'.join(data))
                if return_string == "":
                    return_string += f'- {item}: file_size={file_size} bytes, is_dir={is_dir}'
                else:
                    return_string += f'\n- {item}: file_size={file_size} bytes, is_dir={is_dir}'
            return return_string
            #return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f'Error: {e}'
    print(os.listdir(target_dir))


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
