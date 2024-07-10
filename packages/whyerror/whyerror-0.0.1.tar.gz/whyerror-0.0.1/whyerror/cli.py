import google.generativeai as genai
import click
import keyring
from getpass import getpass


# Define the service name for keyring
SERVICE_NAME = 'whyerror'
API_KEY_NAME = 'GEMINI_API_KEY'


# Set up API key
def configure_gemini(api_key):
    genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')


def get_api_key():

    # Prompt the user for the API key if not found
    api_key = getpass('Enter your Gemini API key: ')
    # Store the API key in keyring
    keyring.set_password(SERVICE_NAME, API_KEY_NAME, api_key)

    return api_key


def make_api_call(prompt):
    """Makes the API call to the Gemini GenerateText endpoint."""

    response = model.generate_content(prompt)

    return response.text



@click.command()
@click.option('-e', '--error', required=True, help='Error message to analyze')
@click.option('-p', '--prompt', required=True, help='Additional prompt message for context')
def whyerror(error, prompt):
    """
    A CLI tool to analyze error messages using OpenAI GPT API.
    """

    # Combine error message and prompt
    combined_prompt = f"""Hey you are my short answer giving agent, here I provide an error and related query.
                    Error message: {error}
                    Prompt: {prompt}
                    
                    You are supposed to give concise and short answers in the following format:
                    
                    \n\nDescription of error: <short and informative description of the error>
                    \nHow to resolve the error?: <answer for resolving the error>
                    \nLook for: <write what I can look for to resolve this error> 
                    \n\n
                    """


    # Call API
    response = make_api_call(combined_prompt)

    print(response)


if __name__ == '__main__':

    api_key = keyring.get_password(SERVICE_NAME, API_KEY_NAME)

    if api_key is None:
        api_key = get_api_key()

    configure_gemini(api_key)

    whyerror()
