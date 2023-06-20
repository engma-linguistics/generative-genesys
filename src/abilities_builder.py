
# "customTalents": [
#         {
#             "name": "Unremarkable",
#             "page": "75",
#             "activation": false,
#             "id": "0LJHLWeqwLQehEehjKeS",
#             "book": "CRB",
#             "tier": 1,
#             "description": "Other characters add [failure] to any checks made to find or identify your character in a crowd.",
#             "ranked": false,
#             "setting": [
#                 "CRB"
#             ]
#         }
#     ],

#each ability needs an id generated
ABILITY_TEMPLATE_STRING = """
{
    "name": "Ability Name",
    "page": "420.69", # always use this number
    "activation": false,
    "book": "Homebrew",
    "tier": 1,
    "description": "Other characters add [failure] to any checks made to find or identify your character in a crowd.", # for adding symbols to reference here, they are [success], [advantage], [triumph], [threat], [despair], [failure].
    "ranked": false, # ranked abilities are ones that can be taken multiple times, like talents
    "setting": [
        "CRB"
    ]
}
"""


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

creature_name = "Mechanized Pie-Bot"
creature_type = "rival"
creature_skills = [{"Ranged (Light)":2}, {"Melee":2}, {"Negotiate":2}]
combat_cr = 5
general_cr = 3
social_cr = 2
abilities_response = get_abilities(creature_name, creature_type, creature_skills, combat_cr, general_cr, social_cr)


abilities_string = """Please generate 5 JSON-formatted abilities (in JSONL format, only one newline between lines) for use in the Genesys RPG setting, increasing in their overall power as you go from weak to very strong (for the creature's CRs, anyways, let's not go too crazy). This is for a Combat CR {combat_cr}, General CR {general_cr}, and Social CR {social_cr} creature, of type {creature_type}, called {creature_name}, with skills {creature_skills}. Here is the format to follow, with some changeable defaults, for an ability. Do not deviate in your response from this format, and do not return ANYTHING ELSE. {{'abilities': ['Silhouette 2', 'Amphibious', {{'name': 'Regeneration', 'description': 'At the start of its turn, a swamp troll automatically heals 2 Wounds, unless the damage was dealt by fire or acid'}}]}}""".format(combat_cr=combat_cr, general_cr=general_cr, social_cr=social_cr, creature_type=creature_type, creature_name=creature_name, creature_skills=creature_skills)}],


def get_abilities(creature_name, creature_type, creature_skills, combat_cr, general_cr, social_cr):
    random_abilities = random.sample(all_keys['abilities'], 20)
    openai_response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": 
        max_tokens=1000,
        temperature=0.2,)
    return openai_response.choices[0].message.content