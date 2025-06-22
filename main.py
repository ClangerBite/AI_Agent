import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt


def get_args():
    return get_prompt(), get_verbose_flag()


def get_prompt():
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not args:
        print("ERROR - No prompt provided")
        sys.exit(1)      
    user_prompt = " ".join(args)
    return user_prompt


def get_verbose_flag():
    return "--verbose" in sys.argv


def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client


def schema():
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
    
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )
    return available_functions

def get_response(client, messages):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(tools =[schema()], system_instruction=system_prompt))
    text = response.text
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count    
    function_call_part = response.function_calls[0]
    return text, prompt_tokens, response_tokens, function_call_part


def print_verbose_content(user_prompt, prompt_tokens,response_tokens):
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
        

def main():
    load_dotenv()
    user_prompt, verbose = get_args()
    client = get_client()

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    
    response, prompt_tokens, response_tokens, function_call_part = get_response(client, messages)
    
    if function_call_part:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response)    
        
    if verbose:
        print_verbose_content(user_prompt, prompt_tokens, response_tokens)
    

if __name__ == "__main__":
    main()