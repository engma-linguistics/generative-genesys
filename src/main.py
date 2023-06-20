from src import openai
import os
import json
import re
from src.base_creature_builder import creature_template_builder
from src.validator import validate_creature, finalization
from src.weapons_builder import weapon_template_builder
from src.utils import fill_template_with_openai, generate_id, upload_new_character, get_character, put_character, get_bearer_token
from src.base_creature_builder import CREATURE_TEMPLATE_DICT
from src.validator import validate_weapon
import logging
logger = logging.getLogger(__name__)
# set logger level to info
logger.setLevel(logging.INFO)


openai.api_key = os.getenv("OPENAI_API_KEY")


def complete_builder(
    creature_description="A goblin that throws pies at people.",
    creature_name="Pie Goblin",
    creature_type="Rival",
    setting_description="A generic fantasy setting with magic and monsters",
    setting_specific_skills=[],
    setting_removed_skils=[],
    skills=[],
    allow_other_skills=False,
    combat_cr=-1,
    social_cr=-1,
    general_cr=-1,
    brawn=-1,
    agility=-1,
    intellect=-1,
    cunning=-1,
    willpower=-1,
    presence=-1,
    number_of_weapons=2,
    number_of_abilities=-1,
):
    final_creature_dict = CREATURE_TEMPLATE_DICT
    print("Getting bearer token")
    try:
        bearer_token = get_bearer_token()
    except Exception as e:
        logger.error(e)
        raise e

    print("Building creature template")
    creature_builder_string = creature_template_builder(
        creature_description=creature_description,
        creature_name=creature_name,
        creature_type=creature_type,
        setting_description=setting_description,
        setting_specific_skills=setting_specific_skills,
        setting_removed_skils=setting_removed_skils,
        skills=skills,
        allow_other_skills=allow_other_skills,
        combat_cr=combat_cr,
        social_cr=social_cr,
        general_cr=general_cr,
        brawn=brawn,
        agility=agility,
        intellect=intellect,
        cunning=cunning,
        willpower=willpower,
        presence=presence,
    )

    print("Filling character template with OpenAI, expect this to take about 30 seconds.")
    generated_character_data = fill_template_with_openai(creature_builder_string)
    print("Validating character data")
    generated_character_data_as_dict = validate_creature(generated_character_data)
    generated_character_data_as_dict['characterDescription'] = creature_description
    final_creature_dict["characters"] = [generated_character_data_as_dict]

    print("Building weapon template")
    weapon_builder_string = weapon_template_builder(
        creature_name=creature_name,
        creature_description=creature_description, 
        creature_type=creature_type, 
        setting_description=setting_description, 
        creature_skills=str(list(generated_character_data_as_dict['masterSkills'].keys())), 
        combat_cr=generated_character_data_as_dict['combatCR'],
        number_of_weapons=number_of_weapons)

    print("Filling weapon template with OpenAI, expect this to take about 30 seconds.")
    generated_weapon_data = fill_template_with_openai(weapon_builder_string)
    print("Validating weapon data")
    generated_weapon_data_as_dict = validate_weapon(generated_weapon_data)
    final_creature_dict["customWeapons"] = generated_weapon_data_as_dict

    print("Adding weapons to character")
    final_creature_dict["characters"][0]["equipmentWeapons"] = {}
    for weapon in generated_weapon_data_as_dict:
        new_name = weapon['name'].replace(' ', '').replace("'", '')  # Remove spaces and apostrophes
        new_name = new_name[0].lower() + new_name[1:]  # Lowercase the first letter
        final_creature_dict["characters"][0]["equipmentWeapons"][weapon['id']] = {"craftsmanship": "",
                        "carried": True,
                        "id": new_name,
                        "equipped": True}

    # TODO: Add abilities
    # abilities_string = abilities_template_builder(
    #     creature_name=creature_name,
    #     creature_description=creature_description,
    #     creature_type=creature_type,
    #     setting_description=setting_description,
    #     creature_skills=creature_skills,
    #     combat_cr=combat_cr,
    #     social_cr=social_cr,
    #     general_cr=general_cr,
    #     number_of_abilities=number_of_abilities,

    # TODO: Add gear generator

    print("Writing character to file")
    with open("creature.json", "w") as f:
        f.write(json.dumps(final_creature_dict))
    f.close()

    print("Uploading character to RPGSessions")
    try:
        character_id = upload_new_character(bearer_token, creature_json_path="creature.json")
    except Exception as e:
        logger.error(e)
        raise e

    print("Getting character from RPGSessions to edit raw data")
    try:
        data = get_character(character_id, bearer_token)
    except Exception as e:
        logger.error(e)
        raise e

    print("Editing character data")
    creature_type = generated_character_data_as_dict["creatureType"]
    soak = generated_character_data_as_dict["soak"]
    wounds_threshold = generated_character_data_as_dict["woundThreshold"]
    strain_threshold = generated_character_data_as_dict["strainThreshold"]
    defense_melee = generated_character_data_as_dict["defenseMelee"]
    defense_ranged = generated_character_data_as_dict["defenseRanged"]
    minion_count = generated_character_data_as_dict["minionCount"]-1
    adversary_level = generated_character_data_as_dict["adversaryLevel"]
    combat_cr = generated_character_data_as_dict["combatCR"]
    social_cr = generated_character_data_as_dict["socialCR"]
    general_cr = generated_character_data_as_dict["generalCR"]

    data["characterType"] = "[character type] {creature_type}".format(creature_type=creature_type.lower())

    data["configuration"] = {
        "diceTheme": "[dice theme] genesys",
        "gameTheme": "[game theme] genesys terrinoth",
        "ndsCharacterType": "[nds character type] {character_type}".format(
            character_type=creature_type.lower()
        ),
        "talentsDisplayType": "[nds character talent display type] list",
        "talentsSignatureAbilitiesEnabled": False,
        "forcePowersDisplayType": "[nds character talent display type] list group",
        "dutyEnabled": False,
        "forceEnabled": False,
        "forceDiceEnabled": False,
        "moralityEnabled": False,
        "obligationEnabled": False,
        "superCharacteristicsEnabled": False,
        "heroicAbilitiesEnabled": False,
        "aemberEnabled": False,
        "favorsEnabled": False,
        "agendasEnabled": False,
        "automations": False,
    }
    data["attributes"] = [
        {"value": soak, "type": "[nds character attribute] soak"},
        {"value": 0, "type": "[nds character attribute] wounds current"},
        {"value": wounds_threshold, "type": "[nds character attribute] wounds threshold"},
        {"value": 0, "type": "[nds character attribute] strain current"},
        {"value": strain_threshold, "type": "[nds character attribute] strain threshold"},
        {"value": defense_ranged, "type": "[nds character attribute] defense ranged"},
        {"value": defense_melee, "type": "[nds character attribute] defense melee"},
        {"value": 0, "type": "[nds character attribute] available xp"},
        {"value": 0, "type": "[nds character attribute] total xp"},
        {"value": 0, "type": "[nds character attribute] money"},
        {"value": 0, "type": "[nds character attribute] encumbrance current"},
        {"value": 5, "type": "[nds character attribute] encumbrance threshold"},
        {"value": 0, "type": "[nds character attribute] force rating committed"},
        {"value": minion_count, "type": "[nds character attribute] current minion count"},
        {"value": minion_count, "type": "[nds character attribute] character count"},
        {"value": adversary_level, "type": "[nds character attribute] adversary level"},
        {"value": combat_cr, "type": "[nds character attribute] combat power level"},
        {"value": social_cr, "type": "[nds character attribute] social power level"},
        {"value": general_cr, "type": "[nds character attribute] general power level"},
        {"value": 0, "type": "[nds character attribute] available aember"},
        {"value": 0, "type": "[nds character attribute] total aember"},
    ]

    # update the character!
    # TODO: Add and remove skills in data as desired
    print("Re-uploading character data to RPGSessions, overwriting existing character we just made")
    put_character(character_id, bearer_token, data)

    print("Done!")