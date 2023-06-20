
import os
import json
import re
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
RPGSESSIONS_EMAIL=os.getenv("RPGSESSIONS_EMAIL")
RPGSESSIONS_PASSWORD=os.getenv("RPGSESSIONS_PASSWORD")


ALL_ADVERSARIES = []
# read adversaries.json into a dict
for each_file in os.listdir('data/adversaries'):
    with open('data/adversaries/'+each_file) as f:
        source = re.search(r'adversaries/(.+)\.json', f.name).group(1)
        if source in ["genesys-misc","genesys-creature-catalogue"]:
            continue
        adversaries = json.load(f)
        for adversary in adversaries:
            adversary['source'] = source
    ALL_ADVERSARIES.extend(adversaries)

ALL_KEYS = {}
for adversary in ALL_ADVERSARIES:
    for each_key in adversary.keys():
        if each_key not in ALL_KEYS:
            ALL_KEYS[each_key] = [adversary[each_key]]
        else:
            if adversary[each_key] not in ALL_KEYS[each_key]:
                ALL_KEYS[each_key].append(adversary[each_key])


attributes = [
    {
        "value": 2,
        "type": "[nds character attribute] soak"
    },
    {
        "value": 0,
        "type": "[nds character attribute] wounds current"
    },
    {
        "value": 12,
        "type": "[nds character attribute] wounds threshold"
    },
    {
        "value": 0,
        "type": "[nds character attribute] strain current"
    },
    {
        "value": 11,
        "type": "[nds character attribute] strain threshold"
    },
    {
        "value": 0,
        "type": "[nds character attribute] defense ranged"
    },
    {
        "value": 0,
        "type": "[nds character attribute] defense melee"
    },
    {
        "value": 0,
        "type": "[nds character attribute] available xp"
    },
    {
        "value": 0,
        "type": "[nds character attribute] total xp"
    },
    {
        "value": 0,
        "type": "[nds character attribute] money"
    },
    {
        "value": 6,
        "type": "[nds character attribute] encumbrance current"
    },
    {
        "value": 7,
        "type": "[nds character attribute] encumbrance threshold"
    },
    {
        "value": 0,
        "type": "[nds character attribute] force rating committed"
    },
    {
        "value": 1,
        "type": "[nds character attribute] character count"
    },
    {
        "value": 0,
        "type": "[nds character attribute] current minion count"
    },
    {
        "value": 2,
        "type": "[nds character attribute] adversary level"
    },
    {
        "value": 3,
        "type": "[nds character attribute] combat power level"
    },
    {
        "value": 1,
        "type": "[nds character attribute] social power level"
    },
    {
        "value": 2,
        "type": "[nds character attribute] general power level"
    },
    {
        "value": 0,
        "type": "[nds character attribute] available aember"
    },
    {
        "value": 0,
        "type": "[nds character attribute] total aember"
    }
]

characteristics = [
    {
        "value": 2,
        "superCharacteristic": False,
        "type": "[nds character characteristic] brawn"
    },
    {
        "value": 3,
        "superCharacteristic": False,
        "type": "[nds character characteristic] agility"
    },
    {
        "value": 2,
        "superCharacteristic": False,
        "type": "[nds character characteristic] intellect"
    },
    {
        "value": 3,
        "superCharacteristic": False,
        "type": "[nds character characteristic] cunning"
    },
    {
        "value": 1,
        "superCharacteristic": False,
        "type": "[nds character characteristic] willpower"
    },
    {
        "value": 1,
        "superCharacteristic": False,
        "type": "[nds character characteristic] presence"
    }
]

skills = [
    {
        "id": "4b6a43b1-0121-4861-9a88-998ea11af900", # I'm nearly sure these are just any UUID, I see same name different ID for different characters
        "name": "Æmbercraft",
        "lookupName": "mbercraft-2514", #note the dropped non-ascii character; the 4 digits after seem to be any ole digits
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] willpower"
    },
    {
        "id": "6b03776e-7ebb-462a-8d45-0d2169570a9d",
        "name": "Alchemy",
        "lookupName": "alchemy-6218",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "d8521764-bb04-438e-a6fa-e35b16892e9a",
        "name": "Arcana",
        "lookupName": "arcana-4309",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] magic",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "69c9affc-c877-4934-9ad7-a0536734ec2b",
        "name": "Astrocartography",
        "lookupName": "astrocartography-8583",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "2f0151a1-4101-4204-a119-c6c5f2e2d4d2",
        "name": "Athletics",
        "lookupName": "athletics-1286",
        "isCareer": True,
        "ranks": 1,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] brawn"
    },
    {
        "id": "d5cd9195-87f1-4ac1-8365-3387a81b2e6a",
        "name": "Brawl",
        "lookupName": "brawl-2229",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] combat",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] brawn"
    },
    {
        "id": "37250323-4163-4ea5-9f59-fad5f10c442a",
        "name": "Charm",
        "lookupName": "charm-4853",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] social",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] presence"
    },
    {
        "id": "bf2c7d8c-4834-472e-8ac6-90afb445a68a",
        "name": "Coercion",
        "lookupName": "coercion-6419",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] social",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] willpower"
    },
    {
        "id": "eb08ee7b-448b-49ba-b38d-bc93e7096520",
        "name": "Computers",
        "lookupName": "computers-9729",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "7338343a-cc49-4d5d-b33a-57d8ac234a52",
        "name": "Cool",
        "lookupName": "cool-4149",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] presence"
    },
    {
        "id": "86cf8f1c-14e9-427c-9941-8504aa4f5a53",
        "name": "Coordination",
        "lookupName": "coordination-9010",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "46d2ee72-44c2-45b8-a047-657550717aa0",
        "name": "Deception",
        "lookupName": "deception-8498",
        "isCareer": True,
        "ranks": 1,
        "skillType": "[nds character skill type] social",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] cunning"
    },
    {
        "id": "1a285ffa-392a-4ecd-8441-f0f57bdf54c6",
        "name": "Discipline",
        "lookupName": "discipline-9048",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] willpower"
    },
    {
        "id": "8003a517-6009-4602-a977-2b8f545170c2",
        "name": "Divine",
        "lookupName": "divine-3410",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] magic",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] willpower"
    },
    {
        "id": "d5191bec-9363-4506-bece-c88b89d7e72c",
        "name": "Driving",
        "lookupName": "driving-4812",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "503d4d70-4c01-4e91-8875-405fa4c0f4d5",
        "name": "Gunnery",
        "lookupName": "gunnery-7251",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] combat",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "edb56a52-ab40-4682-a4f7-c67222ba7874",
        "name": "Knowledge",
        "lookupName": "knowledge-3079",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "982a86d9-647b-4aeb-a12a-a03d5d3f9e3c",
        "name": "Leadership",
        "lookupName": "leadership-1864",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] social",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] presence"
    },
    {
        "id": "3ef2cef9-f2e6-4cf3-b85f-5b076649769c",
        "name": "Mechanics",
        "lookupName": "mechanics-6378",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "dac67678-e614-4522-b4ec-d1435b345a43",
        "name": "Medicine",
        "lookupName": "medicine-7601",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "19277fe0-774b-4306-a740-82b5bc55d472",
        "name": "Melee",
        "lookupName": "melee-4278",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] combat",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] brawn"
    },
    {
        "id": "45aea3e5-c2f9-45f7-9703-6f6bb732dcfb",
        "name": "Melee (Heavy)",
        "lookupName": "melee-heavy-4704",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] combat",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] brawn"
    },
    {
        "id": "55f63c35-2173-4322-8e82-ea75fcc44452",
        "name": "Melee (Light)",
        "lookupName": "melee-light-4966",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] combat",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] brawn"
    },
    {
        "id": "83ee2513-cc65-44f6-9ad8-371b9e2f33be",
        "name": "Negotiation",
        "lookupName": "negotiation-6928",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] social",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] presence"
    },
    {
        "id": "5ac822a9-e069-4ebd-bdfd-cb58e348089d",
        "name": "Operating",
        "lookupName": "operating-5491",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "5f1ca89b-502a-43d4-ba55-7655e419d18f",
        "name": "Perception",
        "lookupName": "perception-9659",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] cunning"
    },
    {
        "id": "d9f1e8d1-36ca-496e-9f5b-a1290ad9d0a2",
        "name": "Piloting",
        "lookupName": "piloting-3652",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "545d9dbb-5b33-4af8-a5b8-899c24418cd3",
        "name": "Primal",
        "lookupName": "primal-3836",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] magic",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] cunning"
    },
    {
        "id": "4fd1ab23-f9c9-4a96-8ebe-305847ae2df8",
        "name": "Ranged",
        "lookupName": "ranged-1547",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] combat",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "7271f28b-c4cd-4fe7-a448-fde9d3e0fa2b",
        "name": "Ranged (Heavy)",
        "lookupName": "ranged-heavy-8540",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] combat",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "531e93ee-7e55-42b9-9809-d582f30251de",
        "name": "Ranged (Light)",
        "lookupName": "ranged-light-1279",
        "isCareer": True,
        "ranks": 2,
        "skillType": "[nds character skill type] combat",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "3f5d933d-4bcb-40e9-a7f3-c9da2c6ffbf3",
        "name": "Resilience",
        "lookupName": "resilience-6725",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] brawn"
    },
    {
        "id": "7ef43ae2-1d2a-48b8-be8c-7410203bdbc5",
        "name": "Riding",
        "lookupName": "riding-6921",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "fccf0db5-ea5f-454d-b6b8-c4bedb62e821",
        "name": "Skulduggery",
        "lookupName": "skulduggery-2583",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] cunning"
    },
    {
        "id": "f9c47091-7bfe-4d8f-bd6d-9623ab7b3e6a",
        "name": "Stealth",
        "lookupName": "stealth-1416",
        "isCareer": True,
        "ranks": 2,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] agility"
    },
    {
        "id": "7ef42bda-1fe4-4667-a87d-c86cf96a5e32",
        "name": "Streetwise",
        "lookupName": "streetwise-6495",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] cunning"
    },
    {
        "id": "79bc5baf-3f92-4e2c-b5da-6f301c75f793",
        "name": "Survival",
        "lookupName": "survival-9802",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] cunning"
    },
    {
        "id": "2f5998b0-256b-4c77-b96e-7c422ddf5a0d",
        "name": "Vigilance",
        "lookupName": "vigilance-7599",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] willpower"
    },
    {
        "id": "64835a30-9a90-477f-98e1-24151363ddcb",
        "name": "Knowledge Adventuring",
        "lookupName": "knowledge-adventuring-8381",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "55787881-c4e1-40fa-9c1e-50a74473d7fd",
        "name": "Knowledge Forbidden",
        "lookupName": "knowledge-forbidden-1379",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "9852042e-c9d1-4735-907a-b27fe7b1ea88",
        "name": "Knowledge Geography",
        "lookupName": "knowledge-geography-4683",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "712eda7a-50a6-4208-bbef-5513a612a117",
        "name": "Knowledge Lore",
        "lookupName": "knowledge-lore-6066",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "529e2844-9b44-4014-83ea-ce2df10e1e5c",
        "name": "Runes",
        "lookupName": "runes-3302",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] magic",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "da4e3725-cbd5-469e-af5a-3d4400c8fd70",
        "name": "Verse",
        "lookupName": "verse-5397",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] magic",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] presence"
    },
    {
        "id": "9031a1d6-415b-4119-9900-17aab50ae705",
        "name": "Computers (Hacking)",
        "lookupName": "computers-hacking-2878",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "d0be4537-5dd3-418c-a6d3-46b200b0b68f",
        "name": "Computers (Sysops)",
        "lookupName": "computers-sysops-9081",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] general",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "48bde36b-552f-4229-a2e9-e4c1fde386a1",
        "name": "Knowledge (Science)",
        "lookupName": "knowledge-science-5145",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "0d4b69d8-7ded-42cc-bb9b-9dfcfdd76ac2",
        "name": "Knowledge (Society)",
        "lookupName": "knowledge-society-5568",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "fc69d077-1354-4244-835b-c2c6b11f907a",
        "name": "Knowledge (The Net)",
        "lookupName": "knowledge-the-net-5388",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "0096c2fd-9a76-44b6-9156-ca708d6cee15",
        "name": "Knowledge Æmber",
        "lookupName": "knowledge-mber-1290",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "7b116535-d6ae-4f01-8381-f7edfca28deb",
        "name": "Knowledge Crucible",
        "lookupName": "knowledge-crucible-7327",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    },
    {
        "id": "e52bae76-b752-4361-947d-0be70c6a6413",
        "name": "Knowledge Culture",
        "lookupName": "knowledge-culture-4405",
        "isCareer": False,
        "ranks": 0,
        "skillType": "[nds character skill type] knowledge",
        "extraDice": [],
        "linkedCharacteristic": "[nds character characteristic] intellect"
    }
]

character_data = {
    "_id": "6491230d4fbaea0966c555b9",
    "createdDate": "2023-06-20T03:54:53.810Z",
    "modifiedDate": "2023-06-20T04:56:16.367Z",
    "status": 1,
    "name": "Pie Goblin",
    "lookupName": "pie goblin",
    "image": "https://unbound-legends.imgix.net/character2/genesys-T-jjr.jpg?auto=format",
    "notes": "",
    "privateNotes": "",
    "rulesSystem": "[rules] nds",
    "characterType": "[character type] minion",
    "configuration": {
        "diceTheme": "[dice theme] genesys",
        "gameTheme": "[game theme] genesys terrinoth",
        "ndsCharacterType": "[nds character type] minion", # here is where I need to select minion rival nemesis player
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
        "automations": False
    },
    "userFavorite": False,
    "clonedCount": 0,
    "clonedFromCharacterId": 'null',
    "importData": {
        "imported": True,
        "importDate": "2023-06-20T03:54:53.812Z",
        "importSource": "[import source] genesys emporium"
    },
    "options": {
        "allowGMControl": False
    },
    "tempClone": False,
    "userId": "5f347ccfba8e0a0012a6cdc9",
    "armor": [],
    "attributes": attributes,
    "characteristics": characteristics,
    "crits": [],
    "details": [
        {
            "value": "",
            "type": "[nds character detail] archetype"
        },
        {
            "value": "",
            "type": "[nds character detail] species"
        },
        {
            "value": "NPC Career",
            "type": "[nds character detail] career"
        },
        {
            "value": "",
            "type": "[nds character detail] specialization"
        },
        {
            "value": "",
            "type": "[nds character detail] age"
        },
        {
            "value": "",
            "type": "[nds character detail] weight"
        },
        {
            "value": "",
            "type": "[nds character detail] height"
        },
        {
            "value": "",
            "type": "[nds character detail] notable features"
        },
        {
            "value": "",
            "type": "[nds character detail] background"
        },
        {
            "value": "",
            "type": "[nds character detail] motivation"
        },
        {
            "value": "",
            "type": "[nds character detail] desire"
        },
        {
            "value": "",
            "type": "[nds character detail] fear"
        },
        {
            "value": "",
            "type": "[nds character detail] strength"
        },
        {
            "value": "",
            "type": "[nds character detail] flaw"
        }
    ],
    "duty": {
        "contributionRanks": 0,
        "duties": []
    },
    "equipment": [],
    "favors": [],
    "forcePowers": {
        "talents": [],
        "trees": [],
        "listGroups": []
    },
    "heroicAbilities": [],
    "modifiers": [],
    "morality": {
        "score": 0,
        "sessionScore": 0,
        "moralities": []
    },
    "obligation": {
        "obligations": []
    },
    "skills": skills,
    "talents": {
        "talents": [
            {
                "id": "f44d9578-a3d4-48dc-855b-bfcf06859a60",
                "name": "Duelist",
                "purchased": True,
                "activationType": "[nds character activation type] passive",
                "description": "See CRB, page 73, for more details.",
                "modifiers": [],
                "ranked": False,
                "ranks": 0,
                "isForceTalent": False,
                "isConflictTalent": False,
                "xpCost": 0
            }
        ],
        "trees": [],
        "listGroups": [],
    },
    "weapons": [
        {
            "id": "51af9822-ec5c-47e3-b79a-ac3efc9d158c",
            "name": "Pie Satchel",
            "lookupName": "pie-satchel-2315",
            "linkedSkillId": "531e93ee-7e55-42b9-9809-d582f30251de",
            "baseDamage": 2,
            "damageAddsBrawn": True,
            "critRating": 5,
            "range": "[nds character range band] short",
            "encumbrance": 2,
            "carrying": True,
            "hardPoints": 0,
            "rarity": 0,
            "restricted": False,
            "cost": "0",
            "equipped": True,
            "modifiers": [
                {
                    "id": "c74859fa-7b34-4016-b888-5d9e8dbe0f9f",
                    "type": "[nds character modifier type] narrative",
                    "name": "LimitedAmmo",
                    "description": "5"
                },
                {
                    "id": "51a1427a-e1f3-4fb9-83bd-877a63fd92de",
                    "type": "[nds character modifier type] narrative",
                    "name": "StunDamage",
                    "description": ""
                }
            ],
            "attachments": [],
            "extraDice": [],
            "description": ""
        },
        {
            "id": "d566d01f-ca1c-4aeb-8de2-11c1dff9930e",
            "name": "Super Pie Launcher",
            "lookupName": "super-pie-launcher-7528",
            "linkedSkillId": "531e93ee-7e55-42b9-9809-d582f30251de",
            "baseDamage": 4,
            "damageAddsBrawn": True,
            "critRating": 4,
            "range": "[nds character range band] medium",
            "encumbrance": 4,
            "carrying": True,
            "hardPoints": 0,
            "rarity": 0,
            "restricted": False,
            "cost": "0",
            "equipped": True,
            "modifiers": [
                {
                    "id": "32c653d1-0862-4b61-9941-eeae4eb62834",
                    "type": "[nds character modifier type] narrative",
                    "name": "LimitedAmmo",
                    "description": "3"
                },
                {
                    "id": "9d7f839f-2254-4eb7-9109-4b49f521f3e4",
                    "type": "[nds character modifier type] narrative",
                    "name": "Blast",
                    "description": "1"
                },
                {
                    "id": "1f793500-bf5d-45fc-8212-4399501cda12",
                    "type": "[nds character modifier type] narrative",
                    "name": "StunDamage",
                    "description": ""
                }
            ],
            "attachments": [],
            "extraDice": [],
            "description": ""
        }
    ]
}