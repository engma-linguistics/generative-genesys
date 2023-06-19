
import os
import json
import re
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


ALL_ADVERSARIES = []
# read adversaries.json into a dict
for each_file in os.listdir('data/adversaries'):
    with open('data/adversaries/'+each_file) as f:
        source = re.search(r'adversaries/(.+)\.json', f.name).group(1)
        if source in ["genesys-misc","genesys-creature-catalogue"]:
            continue
        adversaries = json.load(f)
        for adversary in adversaries:
            adversary['source'] = source
    ALL_ADVERSARIES.extend(adversaries)

ALL_KEYS = {}
for adversary in ALL_ADVERSARIES:
    for each_key in adversary.keys():
        if each_key not in ALL_KEYS:
            ALL_KEYS[each_key] = [adversary[each_key]]
        else:
            if adversary[each_key] not in ALL_KEYS[each_key]:
                ALL_KEYS[each_key].append(adversary[each_key])

