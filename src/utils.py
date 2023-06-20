import secrets
import string
from src import openai, RPGSESSIONS_EMAIL, RPGSESSIONS_PASSWORD, SUPABASE_API_KEY
import requests
import os

session = requests.Session()


def generate_id(length=20):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for i in range(length))


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


def get_character(character_id, bearer_token):
    url = "https://api.rpgsessions.com/character/{character_id}".format(
        character_id=character_id
    )
    headers = {
        "Authorization": "Bearer {bearer_token}".format(bearer_token=bearer_token),
    }

    # Make the request
    response = session.get(url, headers=headers)
    return response.json()

def upload_new_character(bearer_token, creature_json_path="creature.json"):
    url = "https://api.rpgsessions.com/import/emporium"
    headers = {
        "Authorization": "Bearer {bearer_token}".format(bearer_token=bearer_token),
    }

    # Open the JSON file in binary mode
    with open(creature_json_path, 'rb') as f:
        # Create a dictionary that will be sent as the files parameter
        files = {'file': (creature_json_path, f)}

        # Make the request
        response = session.post(url, headers=headers, files=files)

    print(response.json())
    character_id = response.json()[0]['id']
    return character_id


def put_character(character_id, bearer_token, data):
    headers = {
        "Authorization": "Bearer {bearer_token}".format(bearer_token=bearer_token),
    }
    url = "https://api.rpgsessions.com/character/{character_id}".format(
        character_id=character_id
    )
    response = session.put(url=url, headers=headers, json=data)
    return response



def get_bearer_token():
    # log in, go to fromSupabase, copy "token" from Response
    url = "https://hizqwhqbldtldumwvlxi.supabase.co/auth/v1/token?grant_type=password"
    headers = {
        "apikey": SUPABASE_API_KEY,
        "Referer": "https://app.rpgsessions.com/",
    }
    data = {
        "email": RPGSESSIONS_EMAIL,
        "password": RPGSESSIONS_PASSWORD,
        "gotrue_meta_security": {},
    }
    response = session.post(url=url, headers=headers, json=data)
    access_token = response.json()['access_token']
    url = "https://api.rpgsessions.com/auth2/fromSupabase"
    response = session.post(url=url, json={"accessToken":access_token})
    bearer_token = response.json()['token']
    return bearer_token
