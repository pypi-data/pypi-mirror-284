# cli/_cli.py

import argparse
from main import execute_icnc_file

def main():
    parser = argparse.ArgumentParser(description="Run ICNC files with OpenAI or Azure OpenAI.")
    parser.add_argument("filename", type=str, help="The .icnc file to execute.")
    parser.add_argument("api_type", type=str, help="The API type to use (Azure or Normal).")
    
    args = parser.parse_args()
    
    execute_icnc_file(args.filename, args.api_type)

if __name__ == "__main__":
    main()
