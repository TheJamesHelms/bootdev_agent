from functions import get_files_info, get_file_content, run_python_file, write_file
import json
from collections.abc import Callable

available_functions = [
    get_files_info.schema_get_files_info,
    get_file_content.schema_get_file_content,
    run_python_file.schemma_run_python_file,
    write_file.schemma_write_file,
]

def call_function(tool_call, verbose: bool = False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map: dict[str, Callable[..., str]] = {
        "get_file_content": get_file_content.get_file_content,
        "get_files_info": get_files_info.get_files_info,
        "run_python_file": run_python_file.run_python_file,
        "write_file": write_file.write_file,
    }

    if function_name in function_map:
        function_args["working_directory"] = "./calculator"
        #print(f"---------> {function_map[function_name]}{function_args}")
        result = function_map[function_name](**function_args)
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        }
    else:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }
