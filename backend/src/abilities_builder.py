ABILITY_TEMPLATE_STRING = """
{
    "name": "Ability name",
    "tier": 1, # 1-5, 1 is common and simple and 5 is legendary and truly powerful
    "activation": true, # true or false
    "turn": "Active (Action)", # only present for activation true abilities, and one of [Active (Action), Active (Incidental), Active (Maneuver)]
    "ranked": false, # ranked abilities are ones that can be taken multiple times, like talents; this is a boolean.
    "ranks": 1, # 1+ for ranked abilities, 0 for non-ranked abilities
    "description": "Ability description"
}
"""

import random
from src import ALL_KEYS

def ability_template_builder(
    creature_name,
    creature_type,
    creature_skills,
    combat_cr,
    general_cr,
    social_cr,
    setting_description,
    number_of_abilities=5,
):
    if number_of_abilities == -1:
        number_of_abilities = 5
    creature_skills = ", ".join(creature_skills)
    abilities_string = "Please generate {number_of_abilities} JSON-formatted NPC abilities (in JSON format, wrap all entries in a list please) for use in the Genesys RPG setting, increasing in their overall power as you go from weak to very strong (for the creature's CRs and type).\n".format(
        number_of_abilities=number_of_abilities
    )

    abilities_string += "This is for a Combat CR {combat_cr}, General CR {general_cr}, and Social CR {social_cr} creature, of type {creature_type}, called {creature_name}, with skills {creature_skills}. The setting this creature is found in is as follows: {setting_description}\n".format(
        combat_cr=combat_cr,
        general_cr=general_cr,
        social_cr=social_cr,
        creature_type=creature_type,
        creature_name=creature_name,
        creature_skills=creature_skills,
        setting_description=setting_description,
    )

    random_abilities = random.sample(ALL_KEYS["abilities"], 10)
    random_abilities_string = "Here are some sample abilities; their format should NOT be followed for your generation (see below for the format to follow).\n\n"
    for each_ability in random_abilities:
        if not isinstance(each_ability, dict):
            each_ability = each_ability + ": No description."
        else:
            each_ability = each_ability['name'] + ": "+ each_ability["description"]
        random_abilities_string += each_ability + "\n"
    abilities_string += random_abilities_string + "\n"

    abilities_string += """Here is the format to follow, with some changeable defaults, for an ability. Do not deviate in your response from this format, and do not return ANYTHING ELSE.\n{ability_template_string}""".format(
        ability_template_string=ABILITY_TEMPLATE_STRING
    )
    return abilities_string
