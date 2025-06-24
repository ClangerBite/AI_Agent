from email import contentmanager
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from system_prompt import system_prompt
from available_functions import available_functions
from call_function import call_function
from config import MAX_LOOPS


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


def generate_content(client, messages, user_prompt, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(tools =[available_functions()], system_instruction=system_prompt))    
    
    if not response.function_calls:
        return response.text
    
    for candidate in response.candidates:
        messages.append(candidate.content)
        
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    function_responses = []
    if response.function_calls != None:
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            
            if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
            ):
                raise Exception("empty function call result")
            
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            
            function_responses.append(function_call_result.parts[0])        
        
    
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    messages.append(types.Content(role="tool", parts=function_responses))
    

def main():
    load_dotenv()
    user_prompt, verbose = get_args()
    client = get_client()

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    
    loops = 0
    looping = True
    
    while True:
        loops += 1
        if loops> MAX_LOOPS:
            print(f"Maximum iterations ({MAX_LOOPS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, user_prompt, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")


if __name__ == "__main__":
    main()