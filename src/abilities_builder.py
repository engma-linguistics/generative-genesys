# I need to build like the below because I have to import everything as emporium talents
""""customTalents": [
        {
            "activation": false,
            "tier": 1,
            "name": "Dungeoneer",
            "id": "LVQlGGE0DaVy86dwy6ld",
            "description": "After your character makes a Perception, Vigilance, or Knowledge (Adventuring) check to notice, identify, or avoid a threat in a cavern, subterranean ruin, or similar location, your character cancels a number of uncanceled [threat] no greater than your character’s ranks in Dugeoneer.",
            "ranked": true,
            "setting": [
                "Terrinoth"
            ],
            "page": "84",
            "book": "ROT"
        },
        {
            "description": "Each rank of Grit increases your character’s strain threshold by one.",
            "id": "oqcABNYaQ46IElv78tZc",
            "setting": [
                "CRB"
            ],
            "activation": false,
            "ranked": true,
            "page": "73",
            "name": "Grit",
            "book": "CRB",
            "tier": 1
        },
        {
            "ranked": false,
            "setting": [
                "Terrinoth"
            ],
            "book": "ROT",
            "page": "88",
            "name": "Heroic Recovery",
            "turn": "Active (Incidental)", # only present for activation true abilities, and Active (Incidental/Maneuver/Action) 
            "activation": true,
            "tier": 2,
            "description": "When your character acquires this talent, choose one characteristic. Once per encounter, you may spend one Story Point to use this talent to have your character heal strain equal to the rating of the chosen characteristic.",
            "id": "DL1tVXvuATkVPFTBy8Sf"
        },
    ],"""


# each ability needs an id generated


""""masterTalents": {
                "1": {
                    "1": "Duelist"
                },"""


# stolen from json, try it out later
# {
#     "id": "8037cdb7-fc81-45e8-991a-37a86853773e",
#     "name": "Flarp",
#     "purchased": true,
#     "activationType": "[nds character activation type] passive",
#     "description": "",
#     "modifiers": [],
#     "ranked": false,
#     "ranks": 2,
#     "isForceTalent": false,
#     "isConflictTalent": false,
#     "xpCost": 0
# }

# # what the GET data looks like
# [{'id': 'd8697ca3-425f-451b-bfcf-699d7e76ac47',
#     'name': 'Dungeoneer',
#     'purchased': True,
#     'activationType': '[nds character activation type] passive',
#     'description': 'After your character makes a Perception, Vigilance, or Knowledge (Adventuring) check to notice, identify, or avoid a threat in a cavern, subterranean ruin, or similar location, your character cancels a number of uncanceled :g%: no greater than your character’s ranks in Dugeoneer.',
#     'modifiers': [],
#     'ranked': False,
#     'ranks': 0,
#     'isForceTalent': False,
#     'isConflictTalent': False,
#     'xpCost': 0},
#    {'id': '70831a64-bf78-4ea6-a740-7f799b888251',
#     'name': 'Grit',
#     'purchased': True,
#     'activationType': '[nds character activation type] passive',
#     'description': 'Each rank of Grit increases your character’s strain threshold by one.',
#     'modifiers': [],
#     'ranked': False,
#     'ranks': 0,
#     'isForceTalent': False,
#     'isConflictTalent': False,
#     'xpCost': 0},
#    {'id': '7267e883-82a7-42da-9fc6-d4baa56d1ca6',
#     'name': 'Signature Spell',
#     'purchased': True,
#     'activationType': '[nds character activation type] passive',
#     'description': 'When your character gains this talent, decide on a signature spell for them, consisting of a particular magic action and a specific set of one or more effects. When your character casts their signature spell (consisting of the exact combination of action and effects previously chosen), reduce the difficulty of the check by one.',
#     'modifiers': [],
#     'ranked': False,
#     'ranks': 0,
#     'isForceTalent': False,
#     'isConflictTalent': False,
#     'xpCost': 0},
#    {'id': 'd69b4a78-7905-4d97-8027-b1f68e9ee9fd',
#     'name': 'Painful Blow',
#     'purchased': True,
#     'activationType': '[nds character activation type] action',
#     'description': 'When your character makes a combat check, you may voluntarily increase the difficulty by one to use this talent. If the target suffers one or more wounds from the combat check, the target suffers 2 strain each time they perform a maneuver until the end of the encounter.',
#     'modifiers': [],
#     'ranked': False,
#     'ranks': 0,
#     'isForceTalent': False,
#     'isConflictTalent': False,
#     'xpCost': 0},
#    {'id': 'a6f0e1b7-4356-4ab8-bb31-100abc935096',
#     'name': 'Heroic Recovery',
#     'purchased': True,
#     'activationType': '[nds character activation type] action',
#     'description': 'When your character acquires this talent, choose one characteristic. Once per encounter, you may spend one Story Point to use this talent to have your character heal strain equal to the rating of the chosen characteristic.',
#     'modifiers': [],
#     'ranked': False,
#     'ranks': 0,
#     'isForceTalent': False,
#     'isConflictTalent': False,
#     'xpCost': 0}]


# and what it looks like for an NPC with talents and abilities
#'talentsDisplayType': '[nds character talent display type] list group',
# 'listGroups': [{'id': '8b3eb148-8b93-43e2-a942-c3b3e380dd5d',
#     'name': 'Abilities',
#     'talentIds': ['225774f7-3e2e-46c9-a9d5-3e93664d69b8',
#      '53520ffc-29b1-47dc-8174-346fe6ffdc18',
#      'f3ddd557-bf6d-4b4c-9d31-33f08c9f2100',
#      'a428bc0f-5c9e-4e37-989a-aff719637ab3']},
#    {'id': '9ccc9a9d-2eb7-4737-b36e-06b445bf3044',
#     'name': 'Talents',
#     'talentIds': ['9f1d6b3b-87ec-47e4-a8cd-5d3c76ad3b2f',
#      '92d76bb8-3280-4438-a4ef-865a4e349057']}],

# 'talents': {'talents': [{'id': '225774f7-3e2e-46c9-a9d5-3e93664d69b8',
#     'name': 'Flyer',
#     'purchased': True,
#     'activationType': '[nds character activation type] passive',
#     'description': 'This creature can fly.',
#     'modifiers': [],
#     'ranked': False,
#     'ranks': 0,
#     'isForceTalent': False,
#     'isConflictTalent': False,
#     'xpCost': 0}],

ABILITY_TEMPLATE_STRING = """
{
    "name": "Ability name",
    "tier": 1, # 1-5, 1 is common and simple and 5 is legendary and truly powerful
    "activation": true, # true or false
    "turn": "Active (Action)", # only present for activation true abilities, and one of [Active (Action), Active (Incidental), Active(Maneuver)]
    "ranked": false, # ranked abilities are ones that can be taken multiple times, like talents; this is a boolean.
    "ranks": 1, # 1+ for ranked abilities, 0 for non-ranked abilities
    "description": "Ability description"
}
"""

import random
from src import ALL_KEYS, openai
from src.utils import fill_template_with_openai


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
            each_ability = {"name": each_ability, "description": "None provided"}
        random_abilities_string += str(each_ability) + "\n"
    abilities_string += random_abilities_string + "\n"

    abilities_string += """Here is the format to follow, with some changeable defaults, for an ability. Do not deviate in your response from this format, and do not return ANYTHING ELSE.\n{ability_template_string}""".format(
        ability_template_string=ABILITY_TEMPLATE_STRING
    )
    return abilities_string
