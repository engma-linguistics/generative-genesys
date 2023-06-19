skills_list = [
    "Alchemy",
    "Astrocartography",
    "Computers",
    "Driving",
    "Operating",
    "Piloting",
    "Riding",
    "Survival",
    "Arcana",
    "Divine",
    "Primal",
    "Gunnery",
    "Melee",
    "Melee-Heavy",
    "Melee-Light",
    "Ranged",
    "Ranged-Heavy",
    "Ranged-Light",
    "Knowledge"
]

new_skill_template = {"customSkills": [
        {
            "setting": [
                "All"
            ],
            "name": "Knowledge Education",
            "type": "Knowledge",
            "characteristic": "Intellect",
            "id": "lfbVQTJbZbo5b07IMUrk"
        }
    ],
}

def skills_checker(generated_skills):
    for generated_skill in generated_skills:
        if generated_skill not in skills_list:
            
            return False