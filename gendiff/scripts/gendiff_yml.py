#!/usr/bin/env python3
import yaml
import json


def open_files(file_path):
    file = yaml.load(open(file_path), Loader=yaml.FullLoader)
    return file


def get_raw_diff(first, second):
    diff = {}
    ss = set(list(first) + list(second))
    for i in dict.fromkeys(sorted(ss)):
        if not (type(first.get(i)) == dict and type(second.get(i)) == dict):
            if i in first and i in second:
                if first.get(i) == second.get(i):
                    diff['  ' + i] = second.get(i)
                else:
                    diff['- ' + i] = first.get(i)
                    diff['+ ' + i] = second.get(i)
            elif i not in second:
                diff['- ' + i] = first.get(i)
            else:
                diff['+ ' + i] = second.get(i)
        else:
            diff['  ' + i] = get_raw_diff(first[i], second[i])
    return diff


def generate_diff(raw_diff):
    final_diff = str((json.dumps(raw_diff, indent=2,)))
    final_diff = final_diff.replace(',', '').replace('"', '')
    return final_diff
