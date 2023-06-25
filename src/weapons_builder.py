WEAPON_TEMPLATE_STRING = """
{
    "name": "Weapon name", # Don't include the name of the creature in the weapon name, that's redundant
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


def weapon_template_builder(
    creature_name,
    creature_description,
    creature_type,
    setting_description,
    creature_skills,
    combat_cr,
    number_of_weapons=5,
):
    if number_of_weapons == -1:
        number_of_weapons = 5
    if creature_description.endswith("."):
        creature_description = creature_description[:-1]
    creature_skills = str(creature_skills)
    weapon_template = """Please generate {number_of_weapons} JSON-formatted weapons (in JSON format, wrap all entries in a list please) for use in the Genesys RPG setting, increasing in their overall power as you go from weak to very strong (for the creature's CR, anyways, let's not go too crazy). Weapons should be varied, not just variations on one theme, and magical creatures ought use one of the magic skills (Arcana, Divine, Runes, Verse, Primal) for at least one weapon. This is for a creature, of type {creature_type}, with a Combat CR of {combat_cr}, called {creature_name}. It can be described as {creature_description}. The setting description this is from is as follows: {setting_description} The creature has the following skills you should consider in making the weapons: {creature_skills}. Following is the format for you to follow, with some changeable defaults, for a weapon. Do NOT deviate in your response from this format, including hallucinating any new fields, and do not return ANYTHING ELSE.\n""".format(
        combat_cr=combat_cr,
        creature_type=creature_type,
        creature_name=creature_name,
        creature_skills=creature_skills,
        creature_description=creature_description,
        setting_description=setting_description,
        number_of_weapons=str(number_of_weapons),
    )
    weapon_template += WEAPON_TEMPLATE_STRING
    weapon_template += "\nFor item qualities, here are the valid options; for all values, lower is cheaper/more-common unless otherwise specified: Accurate (1-5, 1 normal), Auto-Fire, Blast (1-10, often 3-6), Breach (1-3, usually just 1), Burn (1-5, usually 1-3), Concussive (1-5), Cumbersome (3-5), Defensive (1-3), Deflection (1-4), Disorient (1-5, usually 2-3), Ensnare (1-5), Guided (1-5, 4-5 is exceedingly rare outside of advanced guided missiles), Inaccurate (1-3, usually 1), Inferior, Knockdown, Limited Ammo (1 for a grenade-type item, usually 2-4 for missile-type; don't use this for things like bows and arrows though, specifically only for items with a very limited amount of ammo), Linked, Pierce (1-5), Prepare (1-4 and usually only on bigger siege-type or complicated weapons), Reinforced, Slow-Firing (2-4, only on weapons with a need for a big cooldown/recharge), Stun (1-9, just like damage but to strain), Stun Damage, Sunder, Superior, Tractor (only for ship-type weapons, just like ensnare), Unwieldy (3-5), Vicious (1-6, usually 1-2)."

    return weapon_template


# TODO: add an option to load in random weapons from the file
