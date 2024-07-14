# main.py

import os
from dotenv import load_dotenv
import openai  # Assuming you have the OpenAI Python package installed

# Load environment variables
load_dotenv()

def execute_icnc_file(filename):
    # Load OpenAI API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if openai.api_key is None:
        print("OpenAI API key not found in .env file.")
        return
    
    # Read .icnc file
    with open(filename, "r") as file:
        code = file.read()
    
    # Process the code using restricted_eval or any other safe evaluation method
    result = restricted_eval(code)
    
    # Print or process the result as needed
    if result is not None:
        print("Execution result:", result)
    else:
        print("Error executing .icnc file.")

def restricted_eval(code):
    """
    Evaluate Python code in a restricted environment.
    """
    # Define a restricted set of built-in functions and modules accessible
    restricted_globals = {
        '__builtins__': {},
        'math': None,  # Example: Allow access to the math module
        'json': None   # Example: Allow access to the json module
        # Add other safe modules or functions as needed
    }
    
    # Create a local namespace for execution
    local_vars = {}

    try:
        # Execute the code in the restricted environment
        exec(code, restricted_globals, local_vars)
        
        # Return the result if needed
        return local_vars.get('result', None)  # Example: Retrieve 'result' from executed code
    except Exception as e:
        # Handle any exceptions raised during execution
        print(f"Error executing code: {e}")
        return None
