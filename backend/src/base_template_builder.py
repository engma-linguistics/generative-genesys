class BaseTemplate():
    def __init__():
        # inits are all the shared-across-all fields


class CreatureTemplate(BaseTemplate):
    def __init__(self):
        super().__init__()
        # creature-specific inits

def base_template_builder(
    creature_description="A goblin that throws pies at people.",
    creature_name="Pie Goblin",
    creature_type="Rival",
    setting_description="A generic fantasy setting with magic and monsters",
    setting_specific_skills=[],
    setting_removed_skils=[],
    skills=[],
    allow_other_skills=False,
    # silhouette=2,
    combat_cr=-1,
    social_cr=-1,
    general_cr=-1,
    brawn=-1,
    agility=-1,
    intellect=-1,
    cunning=-1,
    willpower=-1,
    presence=-1,
):
    if creature_type not in ["Minion", "Rival", "Nemesis"]:
        raise ValueError("creature_type must be one of Minion, Rival, or Nemesis")
    # if silhouette not in range(1, 10):
    #    raise ValueError("silhouette must be between 1 and 9, inclusive")
    if combat_cr not in range(1, 21) and combat_cr != -1:
        raise ValueError("combat_cr must be between 1 and 20, inclusive")
    if social_cr not in range(1, 21) and social_cr != -1:
        raise ValueError("social_cr must be between 1 and 20, inclusive")
    if general_cr not in range(1, 21) and general_cr != -1:
        raise ValueError("general_cr must be between 1 and 20, inclusive")
    if brawn not in range(1, 7) and brawn != -1:
        raise ValueError("brawn must be between 1 and 6, inclusive")
    if agility not in range(1, 7) and agility != -1:
        raise ValueError("agility must be between 1 and 6, inclusive")
    if intellect not in range(1, 7) and intellect != -1:
        raise ValueError("intellect must be between 1 and 6, inclusive")
    if cunning not in range(1, 7) and cunning != -1:
        raise ValueError("cunning must be between 1 and 6, inclusive")
    if willpower not in range(1, 7) and willpower != -1:
        raise ValueError("willpower must be between 1 and 6, inclusive")
    if presence not in range(1, 7) and presence != -1:
        raise ValueError("presence must be between 1 and 6, inclusive")
    # if creature name ends with punctuation, remove it
    if creature_name[-1] in [".", ",", "!", "?"]:
        creature_name = creature_name[:-1]
    # same for description
    if creature_description[-1] in [".", ",", "!", "?"]:
        creature_description = creature_description[:-1]
    # same for setting description
    if setting_description[-1] in [".", ",", "!", "?"]:
        setting_description = setting_description[:-1]

    creature_template = """Please generate a creature for the Genesys RPG system for me. It is called {creature_name}, and can be described as follows: {creature_description}. Its adversary type is '{creature_type}'. Any references to D&D or other non-Genesys systems in these instructions should be only used as context, do NOT generate anything with D&D stats.\n""".format(
        creature_name=creature_name,
        creature_description=creature_description,
        creature_type=creature_type,
    )

    setting_template = (
        """It is from the following setting: {setting_description}.\n\n""".format(
            setting_description=setting_description
        )
    )
    creature_template += setting_template

    if setting_specific_skills:
        setting_specific_skills_template = """This setting has the following specific non-standard skills you can consider: {setting_specific_skills}.""".format(
            setting_specific_skills=setting_specific_skills
        )
        creature_template += setting_specific_skills_template

    if setting_removed_skils:
        setting_removed_skils_template = """This setting has removed the following skills from the standard Genesys skill list, do not use them: {setting_removed_skils}.""".format(
            setting_removed_skils=setting_removed_skils
        )
        creature_template += setting_removed_skils_template

    if skills:
        skills_template = """The {creature_name} has the following pre-specified skills I want you to include: {skills}.""".format(
            creature_name=creature_name, skills=skills
        )
        creature_template += skills_template
    if allow_other_skills:
        creature_template += " Feel free to add other skills as you see fit. Minions usually have around 1-3 skills, Rivals 2-6, and Nemeses 4-9.\n\n"
    else:
        creature_template += " Do not add any other skills.\n\n"

    #silhouette_template = """It is Silhouette {silhouette} in size. Silhouette 1 is significantly smaller than a person, like a dog or smaller, 2 is around a person's size, 3 is roughly horse-sized, 4 is going to be most dragons or large vehicles, and 5+ usually isn't used for creatures that aren't impossibly large. 10, the largest silhouette, is the size of a moon.\n\n""".format(
    #    silhouette=silhouette
    #)
    #template += silhouette_template

    if combat_cr != -1 or social_cr != -1 or general_cr != -1:
        cr_template = """It has the following CRs (for your use only, do not include them in the JSON!): """
        if combat_cr != -1:
            cr_template += "Combat CR " + str(combat_cr) + ", "
        else:
            cr_template += "Combat CR TBD, "
        if social_cr != -1:
            cr_template += "Social CR " + str(social_cr) + ", "
        else:
            cr_template += "Social CR TBD, "
        if general_cr != -1:
            cr_template += "General CR " + str(general_cr) + ".\n\n"
        else:
            cr_template += "General CR TBD.\n\n"
    else:
        cr_template = """It has unknown Combat, Social, and General CRs, so in generating the creature just use the description and name to estimate how powerful it should be.\n\n"""
    creature_template += cr_template

    weapons_and_abilities_template = (
        "Generate something without weapons or abilities, we'll add those in later.\n\n"
    )
    creature_template += weapons_and_abilities_template

    if (
        brawn != -1
        or agility != -1
        or intellect != -1
        or cunning != -1
        or willpower != -1
        or presence != -1
    ):
        characteristics_template = """It has the following Characteristic ratings:\n"""
        if brawn != -1:
            characteristics_template += "Brawn: " + str(brawn) + ",\n"
        else:
            characteristics_template += "Brawn: TBD,\n"
        if agility != -1:
            characteristics_template += "Agility: " + str(agility) + ",\n"
        else:
            characteristics_template += "Agility: TBD,\n"
        if intellect != -1:
            characteristics_template += "Intellect: " + str(intellect) + ",\n"
        else:
            characteristics_template += "Intellect: TBD,\n"
        if cunning != -1:
            characteristics_template += "Cunning: " + str(cunning) + ",\n"
        else:
            characteristics_template += "Cunning: TBD,\n"
        if willpower != -1:
            characteristics_template += "Willpower: " + str(willpower) + ",\n"
        else:
            characteristics_template += "Willpower: TBD,\n"
        if presence != -1:
            characteristics_template += "Presence: " + str(presence) + ".\n"
        else:
            characteristics_template += "Presence: TBD.\n"
    else:
        characteristics_template = """It has unknown Genesys RPG Characteristic ratings (Brawn, Agility, Intellect, Cuning, Willpower, and Presence; all must be 1-6 and generally only 1-5), please generate them yourself, keeping in mind any specified CRs.\n"""
    creature_template += characteristics_template + "\n"

    creature_template += """The format for your returned creature is as follows:\n"""
    creature_template += CHARACTER_TEMPLATE_STRING
    creature_template += "\nONLY return the JSON object as specified above, (using ONLY the fields from the example), and from the instructions above, NOTHING else. Remember that all generation must be compatible with the Genesys RPG ruleset. All TBD values should be filled in by you with reasonable values."

    return creature_template