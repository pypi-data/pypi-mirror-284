import click
import keyring
from getpass import getpass
import google.generativeai as genai

# Define the service name and API key name
SERVICE_NAME = 'whyerror'
API_KEY_NAME = 'GEMINI_API_KEY'

# Set up Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')


def configure_gemini(api_key):
    """Configure the Gemini API with the provided API key."""
    genai.configure(api_key=api_key)


def get_api_key():
    """Prompt the user for the Gemini API key and store it in keyring."""
    api_key = getpass('Enter your Gemini API key: ')
    keyring.set_password(SERVICE_NAME, API_KEY_NAME, api_key)
    return api_key


def make_api_call(prompt):
    """Make the API call to Gemini's GenerateText endpoint."""
    response = model.generate_content(prompt)
    return response.text


@click.group()
def cli():
    """CLI tool to analyze error messages using OpenAI GPT API."""


@cli.command()
@click.option('-e', '--error', required=True, help='Error message to analyze')
@click.option('-p', '--prompt', required=True, help='Additional prompt message for context')
def analyze(error, prompt):
    """Analyze error messages using OpenAI GPT API."""
    api_key = keyring.get_password(SERVICE_NAME, API_KEY_NAME)
    if api_key is None:
        api_key = get_api_key()
    configure_gemini(api_key)

    combined_prompt = f"""Hey you are my short answer giving agent, here I provide an error and related query.
                    Error message: {error}
                    Prompt: {prompt}
                    
                    You are supposed to give concise and short answers in the following format:
                    
                    \n\nDescription of error: <short and informative description of the error>
                    \nHow to resolve the error?: <answer for resolving the error>
                    \nLook for: <write what I can look for to resolve this error> 
                    \n\n
                    """
    
    response = make_api_call(combined_prompt)
    print(response)


@cli.command('delete_gemini_key')
# @click.command('delete_gemini_key')
def delete_gemini_key():
    """Delete the Gemini API key stored in keyring."""
    try:
        keyring.delete_password(SERVICE_NAME, API_KEY_NAME)
        print('Gemini API key deleted successfully.')
    except keyring.errors.PasswordDeleteError:
        print('No Gemini API key found to delete.')


if __name__ == '__main__':
    cli()

