#!/usr/bin/env python3
import argparse
from . import gendiff_yml
from . import gendiff_json
from . import stylish_format
from . import plain_format
from . import json_format


def generate_diff(first, second):
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
            diff["Value"] = generate_diff(first[i], second[i])
            data_list[i] = diff
    return data_list


def main():
    parser = argparse.ArgumentParser(description=f'{"Compares "}'
                                                 f'{" two configuration"}'
                                                 f'{" files and shows a "}'
                                                 f'{" difference."}')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output', default=stylish_format)
    args = parser.parse_args()
    files = [args.first_file] + [args.second_file]
    for i in range(len(files)):
        if str(files[i]).endswith('.json'):
            files[i] = gendiff_json.open_files(files[i])
        elif str(files[i]).endswith('.yml') or str(files[i]).endswith('.yaml'):
            files[i] = gendiff_yml.open_files(files[i])
    if args.format == "plain":
        print(plain_format.plain(plain_format.same_deleter(
            generate_diff(files[0], files[1]))))
    elif args.format == "json":
        print(json_format.json_(generate_diff(files[0], files[1])))
    else:
        print(stylish_format.stylish(generate_diff(files[0], files[1])))


if __name__ == "__main__":
    main()
