#!/usr/bin/env python3
import argparse
from . import stylish_format
from . import plain_format
from . import json_format
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
    filepaths = [args.first_file] + [args.second_file]
    formater = args.format
    return filepaths, formater


def open_files(filepaths):
    for i in range(len(filepaths)):
        if str(filepaths[i]).endswith('.json'):
            filepaths[i] = [json.load(open(filepaths[i]))]
        elif str(filepaths[i]).endswith('.yml') or str(
                filepaths[i]).endswith('.yaml'):
            filepaths[i] = [yaml.load(open(filepaths[i]),
                            Loader=yaml.FullLoader)]
    return [item for sublist in filepaths for item in sublist]


def generate_diff(files):
    first, second = files
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
            diff["Value"] = generate_diff([first[i], second[i]])
            data_list[i] = diff
    return data_list


def print_final(arguments):
    filepaths, format_type = arguments
    if format_type == "plain":
        print(plain_format.plain(plain_format.same_deleter(
            generate_diff(open_files(filepaths)))))
    elif format_type == "json":
        print(json_format.json_(generate_diff(open_files(filepaths))))
    else:
        print(stylish_format.stylish(generate_diff(open_files(filepaths))))


def main():
    print_final(get_arguments())


if __name__ == "__main__":
    main()
