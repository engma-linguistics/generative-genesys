import openai
import os
import json
import re
from src.base_creature_builder import creature_template_builder
from src.validator import validate_creature, finalization
from src.weapons_builder import weapon_template_builder
from src.utils import fill_template_with_openai, generate_id
from src.base_creature_builder import CREATURE_TEMPLATE_DICT
from src.validator import validate_weapon


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
    generated_character_data = fill_template_with_openai(creature_builder_string)
    generated_character_data_as_dict = validate_creature(generated_character_data)
    final_creature_dict["characters"] = [generated_character_data_as_dict]

    creature_skills = generated_character_data_as_dict["careerSkillsRank"]
    weapon_builder_string = weapon_template_builder(
        creature_name,
        creature_description,
        creature_type,
        setting_description,
        creature_skills,
        combat_cr,
        number_of_weapons=number_of_weapons,
    )

    generated_weapon_data = fill_template_with_openai(weapon_builder_string)

    generated_weapon_data_as_dict = validate_weapon(generated_weapon_data)
    final_creature_dict["customWeapons"] = generated_weapon_data_as_dict

    final_creature_dict["characters"][0]["equipmentWeapons"] = {}
    for weapon in generated_weapon_data_as_dict:
        new_name = weapon["name"].replace(" ", "")  # Remove spaces
        new_name = new_name[0].lower() + new_name[1:]  # Lowercase the first letter
        final_creature_dict["characters"][0]["equipmentWeapons"][weapon["id"]] = {
            "craftsmanship": "",
            "carried": True,
            "id": new_name,
            "equipped": True,
        }

    abilities_string = abilities_template_builder(
        creature_name=creature_name,
        creature_description=creature_description,
        creature_type=creature_type,
        setting_description=setting_description,
        creature_skills=creature_skills,
        combat_cr=combat_cr,
        social_cr=social_cr,
        general_cr=general_cr,
        number_of_abilities=number_of_abilities,


    with open("creature.json", "w") as f:
        f.write(json.dumps(final_creature_dict))
    f.close()