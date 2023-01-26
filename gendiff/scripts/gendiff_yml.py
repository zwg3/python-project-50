#!/usr/bin/env python3
import yaml
import json
import copy


def open_files(file_path):
    file = yaml.load(open(file_path), Loader=yaml.FullLoader)
    return file


def get_raw_diff_for_existing(first, second):
    raw_diff_existing = {}
    for i in sorted(first):
        if i in second:
            if first.get(i) == second.get(i):
                raw_diff_existing['  ' + i] = second.get(i)
            elif first.get(i) != second.get(i):
                raw_diff_existing['- ' + i] = first.get(i)
                raw_diff_existing['+ ' + i] = second.get(i)
        else:
            raw_diff_existing['- ' + i] = first.get(i)
    return raw_diff_existing


def get_raw_diff_for_missing(first, second, raw_diff_existing):
    raw_diff_missing = copy.deepcopy(raw_diff_existing)
    for i in second:
        if i not in first:
            raw_diff_missing['+ ' + i] = second.get(i)
    return raw_diff_missing


def generate_diff(raw_diff):
    raw_diff = str(json.dumps(raw_diff, indent=2,))
    final_diff = raw_diff.replace(',', '').replace('"', '')
    return final_diff
