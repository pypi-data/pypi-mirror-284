import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import re

# Load environment variables
load_dotenv()

def restricted_eval(code):
    # Define a restricted execution environment
    exec_globals = {}
    exec_locals = {}

    try:
        # Execute the code in the restricted environment
        exec(code, exec_globals, exec_locals)
        
        # Return the value of 'result' if it exists
        return exec_locals.get('result', None)
    except Exception as e:
        print(f"Error executing code: {e}")
        return None

def setup_openai_client(api_type):
    if api_type.lower() == 'azure':
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
        client = AzureOpenAI(
            api_key=api_key,
            api_version="2023-07-01-preview",
            azure_endpoint=api_base,
            azure_deployment="shinobi",
        )
        if not api_key or not api_base:
            print("Azure OpenAI API key or endpoint not found in .env file.")
            return None
    elif api_type.lower() == 'normal':
        api_key = os.getenv("OPENAI_API_KEY")
        client = openai.ChatCompletion(api_key=api_key)
        if not api_key:
            print("OpenAI API key not found in .env file.")
            return None
    else:
        print("Invalid API type. Please enter 'Azure' or 'Normal'.")
        return None
    return client

def clean_code(code):
    # Remove code block markers and any language hints
    code = re.sub(r"```[\w]*\n", "", code)
    code = re.sub(r"```", "", code)
    
    # Remove any unnecessary whitespace or non-code related HTML tags
    code = re.sub(r'<\s*lang="en"\s*>', '', code)
    
    # Strip leading/trailing whitespace from each line to clean up the code
    code = "\n".join(line.strip() for line in code.splitlines())

    # Re-indent the code correctly
    indent_level = 0
    formatted_code = []
    for line in code.splitlines():
        stripped_line = line.strip()
        if stripped_line:
            if stripped_line.endswith(':'):
                formatted_code.append('    ' * indent_level + stripped_line)
                indent_level += 1
            elif stripped_line.startswith('return') or stripped_line.startswith('pass'):
                indent_level -= 1
                formatted_code.append('    ' * indent_level + stripped_line)
            else:
                formatted_code.append('    ' * indent_level + stripped_line)
        else:
            formatted_code.append('')
    
    return "\n".join(formatted_code)


def execute_icnc_file(filename, api_type):
    client = setup_openai_client(api_type)
    if not client:
        return
    
    # Read the .icnc file content
    with open(filename, "r") as file:
        icnc_code = file.read()

    # Read the default prompt
    with open("prompts/default_prompt.txt", "r") as file:
        prompt = file.read()

    # Combine the prompt with the .icnc file content
    combined_prompt = prompt + "\n" + icnc_code

    # Pass the combined content to the OpenAI client
    chat_completion = client.chat.completions.create(
        model="text-davinci-003",  # Replace with your model
        messages=[
            {"role": "user", "content": combined_prompt}
        ],
        max_tokens=500,
        stop=None,
        logit_bias={"1734": -100}
    )

    # Extract the generated code from the response
    generated_code = chat_completion.choices[0].message.content
    # Clean the generated code
    cleaned_code = clean_code(generated_code)

    # Evaluate the cleaned code using the custom evaluation function
    restricted_eval(cleaned_code)
