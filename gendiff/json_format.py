import json


def json_(dict_data):
    print(dict_data)
    return json.dumps(dict_data, indent=4)
