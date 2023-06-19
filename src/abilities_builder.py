
abilities_template = 
{"abilities": [ # list of len 0-5, each entry is either a string or a dict, see below for example
    "Silhouette 2", # an example of an ability with a value within its string; most creatures have a Silhouette.
    "Amphibious", # an example of an ability without a value within its string
    {
        "name": "Regeneration",
        "description": "At the start of its turn, a swamp troll automatically heals 2 Wounds, unless the damage was dealt by fire or acid"
    }, # an example of an ability with a name and description
],}


creature_name = "Mechanized Pie-Bot"
creature_type = "rival"
creature_skills = [{"Ranged (Light)":2}, {"Melee":2}, {"Negotiate":2}]
combat_cr = 5
general_cr = 3
social_cr = 2
abilities_response = get_abilities(creature_name, creature_type, creature_skills, combat_cr, general_cr, social_cr)



def get_abilities(creature_name, creature_type, creature_skills, combat_cr, general_cr, social_cr):
    random_abilities = random.sample(all_keys['abilities'], 20)
    openai_response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": """Please generate 5 JSON-formatted abilities (in JSONL format, only one newline between lines) for use in the Genesys RPG setting, increasing in their overall power as you go from weak to very strong (for the creature's CRs, anyways, let's not go too crazy). This is for a Combat CR {combat_cr}, General CR {general_cr}, and Social CR {social_cr} creature, of type {creature_type}, called {creature_name}, with skills {creature_skills}. Here is the format to follow, with some changeable defaults, for an ability. Do not deviate in your response from this format, and do not return ANYTHING ELSE. {{'abilities': ['Silhouette 2', 'Amphibious', {{'name': 'Regeneration', 'description': 'At the start of its turn, a swamp troll automatically heals 2 Wounds, unless the damage was dealt by fire or acid'}}]}}""".format(combat_cr=combat_cr, general_cr=general_cr, social_cr=social_cr, creature_type=creature_type, creature_name=creature_name, creature_skills=creature_skills)}],
        max_tokens=1000,
        temperature=0.2,)
    return openai_response.choices[0].message.content