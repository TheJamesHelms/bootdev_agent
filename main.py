import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
import call_function
from functions import get_files_info, get_file_content, run_python_file, write_file
import json

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("no api key found")



def main():
    print("Hello from agent!")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    #print(f"verbose: {args.verbose}")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    client = OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key = api_key,
    )
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=call_function.available_functions,
        )
        #print(f"Prompt tokens: {response.usage.prompt_tokens}")
        #print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)
        result_message = ""

        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                #print(f"Calling function: {tool_call.function.name}({function_args})")
                result_message = call_function.call_function(tool_call, args.verbose)
                if not result_message['content']:
                    raise Exception("Error: tool call returned no content")
                if args.verbose:
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
        else:
            print(response.choices[0].message.content)
            break
        #print(_)
        if _ == 19:
            print("Error: failed to return a final message withing loop limit")
            exit(1)




if __name__ == "__main__":
    main()
