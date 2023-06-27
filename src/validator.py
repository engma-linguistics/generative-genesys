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
        if each_weapon["qualities"] != {}: # if not empty
            new_qualities = {}
            for quality_key, quality_value in each_weapon["qualities"]:
                # Accurate (1-5, 1 normal), Auto-Fire, Blast (1-9, often 3-6), Breach (1-3, usually just 1), Burn (1-5, usually 1-3), Concussive (1-5), Cumbersome (3-5), Defensive (1-3), Deflection (1-4), Disorient (1-5, usually 2-3), 
                # Ensnare (1-5), Guided (1-5, 4-5 is exceedingly rare outside of advanced guided missiles), Inaccurate (1-3, usually 1), Inferior, Knockdown, Limited Ammo (1 for a grenade-type item, usually 2-4 for missile-type; 
                # don't use this for things like bows and arrows though, specifically only for items with a very limited amount of ammo), 
                # Linked, Pierce (1-5), Prepare (1-4 and usually only on bigger siege-type or complicated weapons), Reinforced, Slow-Firing (2-4, only on weapons with a need for a big cooldown/recharge), 
                # Stun (1-9, just like damage but to strain), Stun Damage, Sunder, Superior, Tractor (only for ship-type weapons, just like ensnare), Unwieldy (3-5), Vicious (1-6, usually 1-2)."

                if quality_value in ["1", "2", "3", "4", "5", "6", "7" , "8", "9"]:  # shouldn't ever get more'n that
                    
                    new_quality_key = quality_key + " " +quality_value
                elif quality_value == "":
                    new_quality_key = quality_key
                else:
                    print("warning, invalid quality value: ", each_weapon)
                    passes_all_validation_steps = False
                if quality_key == "Accurate":
                    new_quality_value = "Accurate weapons are easier to aim or wield, whether through design or technology. For each level of this quality, the attacker adds :nB: to their combat checks while using this weapon."
                elif quality_key == "Auto-Fire":
                    new_quality_value = "If the attack hits, the attacker can trigger Auto-fire by spending :n^::n^:. Auto-fire can be triggered multiple times. Each time the attacker triggers Auto-fire, it deals an additional hit to the target. Each of these counts as an additional hit from that weapon, and each hit deals base damage plus the number of :n*: on the check. These additional hits can be allocated to the original target, or to other targets within range of the weapon. If the attacker wishes to hit multiple targets, they must decide to do so before making the check. Furthermore, if they wish to hit multiple targets, their initial target must always be the target with the highest difficulty and highest defense (if this is two separate targets, the GM chooses which is the initial target). The initial hit must always be against the initial target. Subsequent hits generated can be allocated to any of the other designated targets. Auto-fire weapons can also activate one Critical Injury for each hit generated on the attack, per the normal rules; the Critical Injury must be applied to the target of the specific hit."
                elif quality_key == "Blast":
                    new_quality_value = "The weapon has a large spread, an explosive blast, or a similar area of effect, like a detonated grenade or a warhead fired from a missile launcher. If the attack is successful and Blast activates, each character (friend or foe) engaged with the original target suffers a hit dealing damage equal to the Blast quality's rating, plus damage equal to the total :n*: scored on the check. In a relatively small and enclosed area, the Game Master might decide that everyone in the room suffers damage. If the Blast quality doesn't activate, the ordnance still detonates, but bad luck or poor aim on the part of the firer (or quick reactions on the part of the targets) means the explosion may not catch anyone else in its radius. However, the user may also trigger Blast if the attack misses by spending aaa. In this case, the original target and every target engaged with the original target suffers a hit dealing damage equal to the Blast rating of the weapon."
                elif quality_key == "Breach":
                    new_quality_value = "Weapons with Breach burn through the toughest armor; they are often heavy weapons or weapons mounted on some sort of vehicle. Hits from weapons with the Breach quality ignore one point of vehicle armor for every rating of Breach (meaning they also ignore 10 soak for every rating of Breach)."
                elif quality_key == "Burn":
                    new_quality_value = "Weapons with Burn inflict damage over time. When Burn is triggered, one target hit by the attack continues to suffer the weapon's base damage each round for a number of rounds equal to the weapon's Burn rating. Apply damage at the start of each of the target's turns. If multiple targets suffer hits from a weapon with Burn, the quality may be triggered multiple times, affecting a different target each time. A victim might be able to stop the damage by performing an action to roll around and make a Coordination check. The difficulty is Average (:nD::nD:) on hard surfaces such as the floor of a building, or an Easy (:nD:) on grass or soft ground. Jumping into a body of water stops the damage immediately. Both situations assume the flame is from actual combustion rather than a chemical reaction. With the latter, there is usually little the victim can do."
                elif quality_key == "Concussive":
                    new_quality_value = ""
                elif quality_key == "Cumbersome":
                    new_quality_value = ""
                elif quality_key == "Defensive":
                    new_quality_value = ""
                elif quality_key == "Deflection":
                    new_quality_value = ""
                elif quality_key == "Disorient":
                    new_quality_value = ""
                elif quality_key == "Ensnare":
                    new_quality_value = ""
                elif quality_key == "Guided":
                    new_quality_value = ""
                elif quality_key == "Inaccurate":
                    new_quality_value = ""
                elif quality_key == "Inferior":
                    new_quality_value = ""
                elif quality_key == "Knockdown":
                    new_quality_value = ""
                elif quality_key == "Limited Ammo":
                    new_quality_value = ""
                elif quality_key == "Linked":
                    new_quality_value = ""
                elif quality_key == "Pierce":
                    new_quality_value = ""
                elif quality_key == "Prepare":
                    new_quality_value = ""
                elif quality_key == "Reinforced":
                    new_quality_value = ""
                elif quality_key == "Slow-Firing":
                    new_quality_value = ""
                elif quality_key == "Stun":
                    new_quality_value = ""
                elif quality_key == "Stun Damage":
                    new_quality_value = ""
                elif quality_key == "Sunder":
                    new_quality_value = ""
                elif quality_key == "Superior":
                    new_quality_value = ""
                elif quality_key == "Tractor":
                    new_quality_value = ""
                elif quality_key == "Unwieldy":
                    new_quality_value = ""
                elif quality_key == "Vicious":
                    new_quality_value = ""
                else:
                    print("warning, invalid quality key, skipping it: ", each_weapon)
                
                
                new_qualities[new_quality_key] = new_quality_value
            each_weapon["qualities"] = new_qualities

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
