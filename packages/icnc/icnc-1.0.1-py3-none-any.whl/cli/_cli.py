# cli/_cli.py

import argparse
import os
from dotenv import load_dotenv
from main import execute_icnc_file
import glob

# Load environment variables
load_dotenv()

def create_missing_files():
    if not os.path.exists(".env"):
        create_env = input("No .env file found. Would you like to create one? (y/n): ")
        if create_env.lower() == "y":
            # Create the .env file with some default content if needed
            with open(".env", "w") as f:
                f.write("OPENAI_API_KEY=<your_openai_api_key>\n")
                f.write("AZURE_OPENAI_API_KEY=<your_azure_openai_api_key>\n")
                f.write("AZURE_OPENAI_ENDPOINT=<your_azure_openai_endpoint>\n")
        else:
            print("Please create a .env file with your API keys.")
            return False
    icnc_files = glob.glob("*.icnc")
    if not icnc_files:
        create_icnc = input("No .icnc file found. Would you like to create one? (y/n): ")
        if create_icnc.lower() == "y":
            # Create the filename.icnc file with some default content if needed
            filename = input("Enter the filename for your ICNC code: ")
            with open(f"{filename}.icnc", "w") as f:
                f.write("# Add your ICNC code here\n")
        else:
            print("Please create a filename.icnc file with your ICNC code.")
            return False

    return True

def main():
    # Check for missing files before proceeding
    if not create_missing_files():
        return  # Exit if files are missing
    
    parser = argparse.ArgumentParser(description="Run ICNC files with OpenAI or Azure OpenAI.")
    parser.add_argument("filename", type=str, help="The .icnc file to execute.")
    parser.add_argument("api_type", type=str, help="The API type to use (Azure or Normal).")
    
    args = parser.parse_args()
    
    execute_icnc_file(args.filename, args.api_type)

if __name__ == "__main__":
    main()
