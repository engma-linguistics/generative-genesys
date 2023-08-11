from flask import Flask, request, jsonify
from flask_cors import CORS
from src.main import complete_builder
from src.utils import get_bearer_token

# import your module
# from your_module import your_function

app = Flask(__name__)
CORS(app)  # to handle cross-origin requests


bearer_token = get_bearer_token()

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    print(data)
    if data['setting_specific_skills'] == '':
        data['setting_specific_skills'] = []
    if data['setting_removed_skils'] == '':
        data['setting_removed_skils'] = []
    if data['skills'] == '':
        data['skills'] = []
    if data['combat_cr'] == '':
        data['combat_cr'] = -1
    if data['social_cr'] == '':
        data['social_cr'] = -1
    if data['general_cr'] == '':
        data['general_cr'] = -1
    if data['brawn'] == '':
        data['brawn'] = -1
    if data['agility'] == '':
        data['agility'] = -1
    if data['intellect'] == '':
        data['intellect'] = -1
    if data['cunning'] == '':
        data['cunning'] = -1
    if data['willpower'] == '':
        data['willpower'] = -1
    if data['presence'] == '':
        data['presence'] = -1
    if data['number_of_weapons'] == '':
        data['number_of_weapons'] = 1
    if data['number_of_abilities'] == '':
        data['number_of_abilities'] = 1
    if data['number_of_talents'] == '':
        data['number_of_talents'] = -1



    for each in data.keys():
        if data[each] == '':
            data[each] = None
        

    final_creature_dict = complete_builder(
        creature_description=data.get("creature_description"),
        creature_name=data.get("creature_name"),
        creature_type=data.get("creature_type"),
        setting_description=data.get("setting_description"),
        setting_specific_skills=data.get("setting_specific_skills"),
        setting_removed_skils=data.get("setting_removed_skils"),
        skills=data.get("skills"),
        allow_other_skills=data.get("allow_other_skills"),
        combat_cr=data.get("combat_cr"),
        social_cr=data.get("social_cr"),
        general_cr=data.get("general_cr"),
        brawn=data.get("brawn"),
        agility=data.get("agility"),
        intellect=data.get("intellect"),
        cunning=data.get("cunning"),
        willpower=data.get("willpower"),
        presence=data.get("presence"),
        number_of_weapons=data.get("number_of_weapons"),
        number_of_abilities=data.get("number_of_abilities"),
        number_of_talents=data.get("number_of_talents"),
        bearer_token=bearer_token,
    )
    
    
    
    # Here, we'll return the transformed data
    return jsonify({"data": final_creature_dict})

if __name__ == '__main__':
    app.run(debug=True)