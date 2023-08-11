TALENT_TEMPLATE_STRING = """
{
    "name": "Talent name",
    "tier": 1, # 1-5, 1 is common and simple and 5 is legendary and truly powerful
    "activation": true, # true or false
    "turn": "Active (Action)", # only present for activation true talents, and one of [Active (Action), Active (Incidental), Active (Maneuver)]
    "ranked": false, # ranked talents are ones that can be taken multiple times, like talents; this is a boolean.
    "ranks": 1, # 1+ for ranked talents, 0 for non-ranked talents
    "description": "Talent description"
}
"""

import random
from src import ALL_KEYS

def talent_template_builder(
    creature_name,
    creature_type,
    creature_skills,
    combat_cr,
    general_cr,
    social_cr,
    setting_description,
    number_of_talents=5,
):
    if number_of_talents == -1:
        number_of_talents = 5
    creature_skills = ", ".join(creature_skills)
    talents_string = "Please generate {number_of_talents} JSON-formatted NPC talents (in JSON format, wrap all entries in a list please) for use in the Genesys RPG setting, increasing in their overall power as you go from weak to very strong (for the creature's CRs and type).\n".format(
        number_of_talents=number_of_talents
    )

    talents_string += "This is for a Combat CR {combat_cr}, General CR {general_cr}, and Social CR {social_cr} creature, of type {creature_type}, called {creature_name}, with skills {creature_skills}. The setting this creature is found in is as follows: {setting_description}\n".format(
        combat_cr=combat_cr,
        general_cr=general_cr,
        social_cr=social_cr,
        creature_type=creature_type,
        creature_name=creature_name,
        creature_skills=creature_skills,
        setting_description=setting_description,
    )

    random_talents = random.sample(ALL_KEYS["talents"], 10)
    random_talents_string = "Here are some sample talents; their format should NOT be followed for your generation (see below for the format to follow).\n\n"
    for each_talent in random_talents:
        if not isinstance(each_talent, dict):
            each_talent = each_talent + ": No description."
        else:
            each_talent = each_talent['name'] + ": "+ each_talent["description"]
        random_talents_string += each_talent + "\n"
    talents_string += random_talents_string + "\n"

    talents_string += """Here is the format to follow, with some changeable defaults, for a talent. Do not deviate in your response from this format, and do not return ANYTHING ELSE.\n{talent_template_string}""".format(
        talent_template_string=TALENT_TEMPLATE_STRING
    )
    return talents_string
