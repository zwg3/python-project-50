#!/usr/bin/env python3
import argparse
import json


def generate_diff(first_file_path, second_file_path):
    first = json.load(open(first_file_path))
    second = json.load(open(second_file_path))
    diff = {}
    for i in sorted(first):
        if i in second:
            if first.get(i) == second.get(i):
                diff[i] = second.get(i)
            elif first.get(i) != second.get(i):
                diff['- ' + i] = first.get(i)
                diff['+ ' + i] = second.get(i)
        else:
            diff['- ' + i] = first.get(i)
    for i in second:
        if i not in first:
            diff['+ ' + i] = second.get(i)

    diff = str(json.dumps(diff, indent=2,))
    diff = diff.replace(',', '').replace('"', '')
    print(diff)


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration' +
                                                 ' files and shows a' +
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == "__main__":
    main()
