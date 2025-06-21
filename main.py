import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types


def get_argvs(argv):
    return get_prompt(argv), verbose_flag_check(argv)


def get_prompt(argv):
    if len(argv) == 1:
        print("ERROR - No prompt provided")
        sys.exit(1)    
    return argv[1]


def verbose_flag_check(argv):
    verbose_flag = False
    if len(argv) == 3:
        if argv[2] == "--verbose":
            verbose_flag = True
    return verbose_flag


def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client

def get_response(client, messages):
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
    text = response.text
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    
    return text, prompt_tokens, response_tokens

def main():

    load_dotenv()

    user_prompt, is_verbose = get_argvs(sys.argv)
    client = get_client()

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    
    text, prompt_tokens, response_tokens = get_response(client, messages)
    
    print(text)        
    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()