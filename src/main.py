import openai
import os
import json
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    # ask the user for things needed to fill in the template, then fill in the template
    
    # show the results, adjust as necessary
    # TODO: take the resulting JSON and edit it directly? Ask OpenAI to do it?

    # generate weapons, abilities, and gear