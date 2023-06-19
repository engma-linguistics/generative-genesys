import secrets
import string
from src import openai

def generate_id(length=20):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))

def fill_template_with_openai(templated_string):
    try:
            openai_response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            messages=[{"role": "user", "content": templated_string}],
            max_tokens=2000,
            temperature=0.1,
        )
    except Exception as e:
        print(e)
        raise e
    response = openai_response.choices[0].message.content
    return response
    
