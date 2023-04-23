import json
import yaml


def extension_checker(filepath):
    extension = filepath[str(filepath).rfind('.'):]
    return extension


def file_reader(opened_file, file_type):
    if file_type == '.json':
        file = json.load(opened_file)
    elif file_type == '.yml' or file_type == '.yaml':
        file = yaml.load(opened_file, Loader=yaml.FullLoader)
    else:
        raise Exception("Please use .json or .yaml files only")
    return file


def file_opener(filepath):
    with open(filepath) as opened_file:
        opened_file = file_reader(opened_file, extension_checker(filepath))
    return opened_file
