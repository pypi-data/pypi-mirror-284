# icnc ( i c no code )
Trying to make a OpenAI wrapper language, that will evaluate simple programs and doesn't need much issues.

### Required:
 - OpenAI API key


## Basic Usage:

### Clone the repo
```
 pip install icnc
```

### Generate .env and .icnc files
```
icnc
```

### Setup the .env file
```env
# For normal OpenAI
OPENAI_API_KEY=your_openai_api_key

# For Azure OpenAI
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-endpoint.azure.com/
AZURE_OPENAI_API_VERSION=2022-12-01
```

### Edit your .icnc file
```
# Add your ICNC code here
```

### Run the ICNC file
```
icnc <your-filename>.icnc <api-type>
```
There are 2 API types:
1. Normal (case insensitive)
2. Azure (case insensitive)

## And with that Output must be generated in the next line, and still you see no code!