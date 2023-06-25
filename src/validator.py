import ast
import json
from src.utils import generate_id

REQUIRED_CHARACTER_FIELDS = [
    "name",
    "careerSkillsRank",
    "masterSkills",
    "creationCharacteristics",
    "creatureType",
    "adversaryLevel",
    "minionCount",
    "combatCR",
    "socialCR",
    "generalCR",
    "woundThreshold",
    "strainThreshold",
    "soak",
    "defenseMelee",
    "defenseRanged",
]
REQUIRED_WEAPON_FIELDS = [
    "name",
    "encumbrance",
    "setting",
    "damage",
    "range",
    "skill",
    "critical",
    "modifier",
    "qualities",
]
REQUIRED_ABILITY_OR_TALENT_FIELDS = [
    "name",
    "activation",
    "tier",
    "description",
    "ranked",
    "ranks",
]


def validate_creature(generated_data):
    try:
        generated_data_as_dict = ast.literal_eval(generated_data)
    except Exception as e:
        print("cannot convert to dict")  # TODO: ask OpenAI to fix this
        raise e
    passes_all_validation_steps = True
    for k in generated_data_as_dict.keys():
        if k not in REQUIRED_CHARACTER_FIELDS:
            print("warning, extraneous field: ", k)
            passes_all_validation_steps = False

    for k in REQUIRED_CHARACTER_FIELDS:
        if k not in generated_data_as_dict.keys():
            print("warning, missing field: ", k)
            passes_all_validation_steps = False
    if passes_all_validation_steps:
        print("passes all creature validation steps")
    generated_data_as_dict["archetype"] = "Npc"
    generated_data_as_dict["career"] = "NpcCareer"
    generated_data_as_dict["theme"] = "ROT"
    for characteristic in generated_data_as_dict["creationCharacteristics"]:
        generated_data_as_dict["creationCharacteristics"][characteristic] -= 1
    return generated_data_as_dict


def validate_weapon(generated_data):
    try:
        generated_data_as_dict = ast.literal_eval(generated_data)
    except Exception as e:
        print("cannot convert to dict")  # TODO: ask OpenAI to fix this
        raise e
    passes_all_validation_steps = True
    for each_weapon in generated_data_as_dict:
        for k in each_weapon.keys():
            if k not in REQUIRED_WEAPON_FIELDS:
                print("warning, extraneous field: ", k)
                passes_all_validation_steps = False

        for k in REQUIRED_WEAPON_FIELDS:
            if k not in each_weapon.keys():
                print("warning, missing field: ", k)
                passes_all_validation_steps = False
        if passes_all_validation_steps:
            print("passes all weapon validation steps")

        each_weapon["id"] = generate_id()

    return generated_data_as_dict


def validate_talent_or_ability(generated_data):
    try:
        generated_data_as_dict = json.loads(generated_data)
    except Exception as e:
        print("cannot convert to dict")  # TODO: ask OpenAI to fix this
        raise e
    passes_all_validation_steps = True

    for each_talent_or_ability in generated_data_as_dict:
        for k in each_talent_or_ability.keys():
            if k not in REQUIRED_ABILITY_OR_TALENT_FIELDS and k != "turn":
                print("warning, extraneous field: ", k)
                passes_all_validation_steps = False

        for k in REQUIRED_ABILITY_OR_TALENT_FIELDS:
            if k not in each_talent_or_ability.keys():
                print("warning, missing field: ", k)
                passes_all_validation_steps = False

        if passes_all_validation_steps:
            print("this passes all talent/ability validation steps")

        each_talent_or_ability["id"] = generate_id()
        each_talent_or_ability["setting"] = ["Homebrew"]
        each_talent_or_ability["prerequisite"] = ""
        each_talent_or_ability["antirequisite"] = ""
        each_talent_or_ability["page"] = "69"
        each_talent_or_ability["book"] = "None"

    return generated_data_as_dict


def finalization(final_dict, image_link=None):
    if image_link:
        final_dict["characters"][0]["description"] = {"image": image_link}
    with open("creature.json", "w") as f:
        f.write(json.dumps(final_dict))
    f.close()
    return final_dict
