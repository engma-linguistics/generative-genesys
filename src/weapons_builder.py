from src.utils import generate_id
from src import openai

weapons_dict = {"customWeapons": []}

WEAPON_TEMPLATE_STRING = """
{
    "name": "Weapon name",
    "encumbrance": 3, # int from 1-8, a dagger or sword or light pistol is 1, a greataxe or hunting rifle is 4, a machine gun is 6, a rocket launcher or portable battering ram is 8
    "setting": [
        "All" # always use this value
    ],
    "damage": "6", # melee weapons have lower values because they add your brawn score; a sword is 3, greatsword is 5, etc. A bow does 7 damage, assault rifle 8, machine gun 10, but their qualities also contribute to their deadliness!
    "range": "Medium", # Engaged, Short, Medium, Long, Extreme; all melee weapons ought be Engaged excepting spears and polearms and whips, which are Short, and everything else has a range beyond that. A Light pistol is Short, a crossbow is Medium, a hunting rifle Long, and only special weapons like sniper rifles ought have Extreme range.
    "skill": "MeleeHeavy", # note that the skill is 'Melee (Heavy)'; for any skill with spaces or special characters, remove them. Usable skills are Brawl, Melee, Melee (Light), Melee (Heavy), Ranged, Ranged (Light), Ranged (Heavy), Gunnery. In cases of magic, use one of Arcana, Divine, Primal, Rune, Verse.
    "critical": 3, # int from 1-6, 3 is pretty common unless the weapon is more-prone to more-critical hits, like a chainsaw or a sniper rifle, and 6 is generally only for things that aren't really weapons, like a shield.
    "modifier": {}, # leave this blank
    "qualities": { # the below are examples of qualities a weapon can have and the format you should use, see the example weapons for more
        "Defensive": "1",
        "Limited Ammo": "2",
        "Pierce": "1",
        "Stun Damage": "" # blank strings for qualities with no value, like Stun Damage
    }
}
"""
# don't forget to add id to the weapons! generate_id() will do it for you


# send openai the weapon_template and ask for 5 options, given a name, type, skills, and combat CR


def weapon_template_builder(creature_name, creature_description, creature_type, setting_description, creature_skills, combat_cr, number_of_weapons=5):
    if creature_description.endswith("."):
        creature_description = creature_description[:-1]
    creature_skills = str(creature_skills)
    weapon_template = """Please generate {number_of_weapons} JSON-formatted weapons (in JSON format, wrap all entries in a list please) for use in the Genesys RPG setting, increasing in their overall power as you go from weak to very strong (for the creature's CR, anyways, let's not go too crazy). This is for a creature, of type {creature_type}, with a Combat CR of {combat_cr}, called {creature_name}. It can be described as {creature_description}. The setting description this is from is as follows: {setting_description} The creature has the following skills you should consider in making the weapons: {creature_skills}. Following is the format for you to follow, with some changeable defaults, for a weapon. Do NOT deviate in your response from this format, including hallucinating any new fields, and do not return ANYTHING ELSE.""".format(combat_cr=combat_cr, creature_type=creature_type, creature_name=creature_name, creature_skills=creature_skills, creature_description=creature_description, setting_description=setting_description, number_of_weapons=str(number_of_weapons))
    weapon_template += WEAPON_TEMPLATE_STRING

    return weapon_template

# TODO: add an option to load in random weapons from the file