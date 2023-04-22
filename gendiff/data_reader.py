import json
import yaml


def file_reader(filepath, opened_file):
    if str(filepath).endswith('.json'):
        file = json.load(opened_file)
    elif str(filepath).endswith('.yml') or str(filepath).endswith('.yaml'):
        file = yaml.load(opened_file, Loader=yaml.FullLoader)
    else:
        raise Exception("Please use .json or .yaml files only")
    return file


def file_opener(filepath):
    with open(filepath) as opened_file:
        opened_file = file_reader(filepath, opened_file)
        return opened_file
