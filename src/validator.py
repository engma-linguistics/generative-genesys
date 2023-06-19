import ast
import json
from src.utils import generate_id

REQUIRED_CHARACTER_FIELDS = ["name", "careerSkillsRank", "masterSkills", "creationCharacteristics"]
REQUIRED_WEAPON_FIELDS = ["name", "encumbrance", "setting", "damage", "range", "skill", "critical", "modifier", "qualities"]

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
        print("passes all validation steps")
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
            print("passes all validation steps")
        
        each_weapon["id"] = generate_id()
    
    return generated_data_as_dict




def finalization(generated_data_as_dict, image_link=None):
    final_dict["characters"] = [generated_data_as_dict]
    if image_link:
        final_dict["characters"][0]["description"] = {"image": image_link}
    with open("creature.json", "w") as f:
        f.write(json.dumps(final_dict))
    f.close()
    return final_dict
