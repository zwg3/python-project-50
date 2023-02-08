#!/usr/bin/env python3
import json
import os

def get_data(first, second):
    ss = set(list(first) + list(second))
    data_list = {}
    for i in dict.fromkeys(sorted(ss)):
        diff = {}
        if not (type(first.get(i)) == dict and type(second.get(i)) == dict):
            if i in first and i in second:
                if first.get(i) == second.get(i):
                    diff["Key"] = i
                    diff["Type"] = "same"
                    diff["Value"] = second.get(i)
                    data_list[i] = diff
                else:
                    diff["Key"] = i
                    diff["Type"] = "changed"
                    diff["Value"] = first.get(i)
                    diff["Value_new"] = second.get(i)
                    data_list[i] = diff
            elif i not in second:
                diff["Key"] = i
                diff["Type"] = "removed"
                diff["Value"] = first.get(i)
                data_list[i] = diff
            else:
                diff["Key"] = i
                diff["Type"] = "added"
                diff["Value"] = second.get(i)
                data_list[i] = diff
        else:
            diff["Key"] = i
            diff["Type"] = "parent"
            diff["Value"] = get_data(first[i], second[i])
            data_list[i] = diff
    return data_list

def open_files(file_path):
    file = json.load(open(file_path))
    return file

f1 = open_files('tests/fixtures/test_json/file3.json')
f2 = open_files('tests/fixtures/test_json/file4.json')

print(f1)

# a = str(get_data(f1, f2))
# print(a)
# with open(os.path.abspath('tests/fixtures/test_json/diff_result_raw.md')) as test_file:
#         test_file = test_file.read().rstrip('\n')
#         print(test_file == a)