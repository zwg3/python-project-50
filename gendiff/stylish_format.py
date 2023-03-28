#!/usr/bin/env python3
import json


def formating_children(parent_d):
    formated_d = {}
    for i in parent_d:
        if parent_d[i]["Type"] == "removed":
            formated_d["- " + parent_d[i]["Key"]] = parent_d[i]["Value"]
        elif parent_d[i]["Type"] == "same":
            formated_d["  " + parent_d[i]["Key"]] = parent_d[i]["Value"]
        elif parent_d[i]["Type"] == "added":
            formated_d["+ " + parent_d[i]["Key"]] = parent_d[i]["Value"]
        elif parent_d[i]["Type"] == "changed":
            formated_d["- " + parent_d[i]["Key"]] = parent_d[i]["Value"]
            formated_d["+ " + parent_d[i]["Key"]] = parent_d[i]["Value_new"]
    return formated_d


def formating_parents(dict_data):
    formated_dict = {}
    for i in dict_data:
        if dict_data[i]["Type"] != "parent":
            formated_dict.update(formating_children(dict_data))
        else:
            formated_dict["  " + dict_data[i]["Key"]] = formating_parents(
                dict_data[i]["Value"])
    return formated_dict


def stylish(raw_data, recursion_depth=0):
    recursion_depth += 1
    stylish_dict = {}
    for i in raw_data:
        if raw_data[i]["Type"] == "parent":
            stylish_dict[" " + raw_data[i]["Key"]] = formating_parents(
                raw_data[i]["Value"])
        else:
            stylish_dict.update(formating_children(raw_data))
    if recursion_depth == 1:
        stylish_dict = json.dumps(stylish_dict,
                                  indent=4).replace(',', '').replace('"', '')
        return stylish_dict
    return stylish_dict
