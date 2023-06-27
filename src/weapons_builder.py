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
        "Defensive": "1", # the values here are strings
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
    weapon_template = """Please generate {number_of_weapons} JSON-formatted weapons (in JSON format, wrap all entries in a list please) for use in the Genesys RPG setting, increasing in their overall power as you go from weak to very strong (for the creature's combat CR). Weapon skills are generally one of [Melee, Brawl, Ranged, Ranged (Light), Ranged (Heavy), Gunnery] though magic-based weapons can instead use [Arcana, Divine, Runes, Verse, Primal]. Weapons should be varied, not just variations on one theme. This is for a creature, of type {creature_type}, with a Combat CR of {combat_cr}, called {creature_name}. It can be described as {creature_description}. The setting description this is from is as follows: {setting_description} The creature has the following skills you should consider in making the weapons: {creature_skills}. Following is the format for you to follow, with some changeable defaults, for a weapon. Do NOT deviate in your response from this format, including hallucinating any new fields, and do not return ANYTHING ELSE.\n""".format(
        combat_cr=combat_cr,
        creature_type=creature_type,
        creature_name=creature_name,
        creature_skills=creature_skills,
        creature_description=creature_description,
        setting_description=setting_description,
        number_of_weapons=str(number_of_weapons),
    )
    weapon_template += WEAPON_TEMPLATE_STRING
    weapon_template += "\nFor item qualities, here are the valid options; for all values, lower is cheaper/more-common unless otherwise specified: Accurate (1-5, 1 normal), Auto-Fire, Blast (1-9, often 3-6), Breach (1-3, usually just 1), Burn (1-5, usually 1-3), Concussive (1-5), Cumbersome (3-5), Defensive (1-3), Deflection (1-4), Disorient (1-5, usually 2-3), Ensnare (1-5), Guided (1-5, 4-5 is exceedingly rare outside of advanced guided missiles), Inaccurate (1-3, usually 1), Inferior, Knockdown, Limited Ammo (1 for a grenade-type item, usually 2-4 for missile-type; don't use this for things like bows and arrows though, specifically only for items with a very limited amount of ammo), Linked, Pierce (1-5), Prepare (1-4 and usually only on bigger siege-type or complicated weapons), Reinforced, Slow-Firing (2-4, only on weapons with a need for a big cooldown/recharge), Stun (1-9, just like damage but to strain), Stun Damage, Sunder, Superior, Tractor (only for ship-type weapons, just like ensnare), Unwieldy (3-5), Vicious (1-6, usually 1-2)."

    return weapon_template


# TODO: add an option to load in random weapons from the file

# below is a weapon with an attribute edit to it; this is an intercepted payload or whatever from editing and submitting on the website. Looks like it has to be added to the data object directly as there's no emporium equiv.
"""[
    {
        "id": "89b512ef-b83c-44f7-8fc8-e894d3655665",
        "name": "Crab Claw",
        "lookupName": "crab-claw-3061",
        "linkedSkillId": "60187713-f4c2-4c21-8848-a17f074576a2",
        "baseDamage": 3,
        "damageAddsBrawn": true,
        "critRating": 4,
        "range": "[nds character range band] engaged",
        "encumbrance": 1,
        "carrying": true,
        "hardPoints": 0,
        "rarity": 0,
        "restricted": false,
        "cost": "0",
        "equipped": true,
        "modifiers": [
            {
                "id": "7753ee76-89d0-404d-a0cb-1bd3f9583448",
                "type": "[nds character modifier type] narrative",
                "name": "Defensive",
                "description": "1"
            },
            {
                "id": "d0632b7e-2d18-437b-92cb-d5c48eedaf43",
                "type": "[nds character modifier type] narrative",
                "name": "Knockdown",
                "description": ""
            },
            {
                "id": "d4f75078-3014-456c-b428-f00bd61dc649",
                "type": "[nds character modifier type] attribute",
                "name": "defensive 1",
                "description": "",
                "modifierAmount": 1,
                "attribute": "[nds character attribute] defense melee"
            }
        ],
        "attachments": [],
        "extraDice": [],
        "description": "proficiency :nP: \nability :nA: \nboost :nB: \nchallenge :nC: \ndifficulty :nD: \nsetback :nK: \nrem. setbck  :nX: \ntriumph :n!: \nsuccess :n*: \nadvantage :n^: \ndespair :n$: \nfailure :n-: \nthreat :n%: \nupgrade positive :nU: \nupgrade negative :nV: "
    },
    {
        "id": "f6836faf-781c-43f0-9536-2175ff3b4bef",
        "name": "Pincher Spear",
        "lookupName": "pincher-spear-4283",
        "linkedSkillId": "60187713-f4c2-4c21-8848-a17f074576a2",
        "baseDamage": 4,
        "damageAddsBrawn": true,
        "critRating": 3,
        "range": "[nds character range band] short",
        "encumbrance": 2,
        "carrying": true,
        "hardPoints": 0,
        "rarity": 0,
        "restricted": false,
        "cost": "0",
        "equipped": true,
        "modifiers": [
            {
                "id": "31ab9f7c-4d86-4b08-a890-44164ac1ce0b",
                "type": "[nds character modifier type] narrative",
                "name": "Pierce",
                "description": "2"
            },
            {
                "id": "4ca0d8fa-7bfb-4c5a-a075-fdd0921e17b2",
                "type": "[nds character modifier type] narrative",
                "name": "Defensive",
                "description": "1"
            }
        ],
        "attachments": [],
        "extraDice": [],
        "description": ""
    },
    {
        "id": "36bc2588-4b65-4755-930b-e4881995b411",
        "name": "Crustacean Maul",
        "lookupName": "crustacean-maul-2599",
        "linkedSkillId": "60187713-f4c2-4c21-8848-a17f074576a2",
        "baseDamage": 6,
        "damageAddsBrawn": true,
        "critRating": 2,
        "range": "[nds character range band] engaged",
        "encumbrance": 4,
        "carrying": true,
        "hardPoints": 0,
        "rarity": 0,
        "restricted": false,
        "cost": "0",
        "equipped": true,
        "modifiers": [
            {
                "id": "98593200-c387-4f60-8fd3-5e6b8f286021",
                "type": "[nds character modifier type] narrative",
                "name": "Knockdown",
                "description": ""
            },
            {
                "id": "e7b6adb4-6767-43e3-929e-3648aec21cad",
                "type": "[nds character modifier type] narrative",
                "name": "Vicious",
                "description": "2"
            },
            {
                "id": "504b7b94-8457-4b51-b516-9361b67794d0",
                "type": "[nds character modifier type] narrative",
                "name": "Defensive",
                "description": "2"
            }
        ],
        "attachments": [],
        "extraDice": [],
        "description": ""
    }
]"""