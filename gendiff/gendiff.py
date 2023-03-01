#!/usr/bin/env python3
import argparse
from . import stylish_format
from . import plain_format
import json
import yaml


def get_arguments():
    parser = argparse.ArgumentParser(description=f'{"Compares "}'
                                                 f'{" two configuration"}'
                                                 f'{" files and shows a "}'
                                                 f'{" difference."}')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output', default='stylish_format')
    args = parser.parse_args()
    filepath1 = args.first_file
    filepath2 = args.second_file
    formater = args.format
    return filepath1, filepath2, formater


def open_files(filepath):
    if str(filepath).endswith('.json'):
        file = json.load(open(filepath))
        return file
    elif str(filepath).endswith('.yml') or str(filepath).endswith('.yaml'):
        file = yaml.load(open(filepath), Loader=yaml.FullLoader)
        return file
    else:
        return filepath


def print_final(arguments):
    filepath1, filepath2, format_type = arguments
    if format_type == "plain":
        print(plain_format.plain(
              plain_format.same_deleter(
                  generate_diff(filepath1, filepath2, format_type))))
    elif format_type == "json":
        print(json.dumps(
            generate_diff(
                filepath1, filepath2, format_type),
            indent=4).replace(',', '').replace('"', ''))
    else:
        print(stylish_format.stylish(
            generate_diff(filepath1, filepath2, format_type)))


def basic_formater(diff_data, depth=""):
    if depth != 1:
        diff_data = json.dumps(
            diff_data, indent=4).replace(',', '').replace('"', '')
    return diff_data


def generate_diff(filepath_1, filepath_2, formater="", depth=""):
    first = open_files(filepath_1)
    second = open_files(filepath_2)
    keys = set(list(first) + list(second))
    data_list = {}
    for i in dict.fromkeys(sorted(keys)):
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
            diff["Value"] = generate_diff(first[i], second[i], '', depth=1)
            data_list[i] = diff
    return data_list


def main():
    print_final(get_arguments())


if __name__ == "__main__":
    main()
