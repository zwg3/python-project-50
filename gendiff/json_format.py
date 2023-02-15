import json


def json_(dict_data):
    return json.dumps(dict_data, indent=4).replace(',', '').replace('"', '')
