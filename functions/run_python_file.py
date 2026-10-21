import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs,file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs,target_file_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python", target_file_path]
            if args:
                command.extend(args)
            comp_proc = subprocess.run(command, cwd=working_directory, capture_output=True,text=True, timeout=30)
            return_str = ""
            if comp_proc.returncode != 0:
                return_str += f"Process exited with code {comp_proc.returncode}"
            elif not comp_proc.stdout and not comp_proc.stderr:
                return_str += "No output produced"
            else:
                return_str += f"STDOUT: {comp_proc.stdout}\n"
                return_str += f"STDERR: {comp_proc.stderr}"

        return return_str


    except Exception as e:
        print(f"Error: {e}")

schemma_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs the python located at the file path provided and passing in the arguments from args",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to python file to run, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Arguments to pass to the function to be called"
                }
            },
        },
    },
}
