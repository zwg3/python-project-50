#!/usr/bin/env python3
import argparse
import json


def open_files(file_path):
    file = json.load(open(file_path))
    return file


def generate_raw_diff(first, second):
    raw_diff = {}
    for i in sorted(first):
        if i in second:
            if first.get(i) == second.get(i):
                raw_diff[i] = second.get(i)
            elif first.get(i) != second.get(i):
                raw_diff['- ' + i] = first.get(i)
                raw_diff['+ ' + i] = second.get(i)
        else:
            raw_diff['- ' + i] = first.get(i)
    for i in second:
        if i not in first:
            raw_diff['+ ' + i] = second.get(i)
    return raw_diff


def generate_diff(raw_diff):
    raw_diff = str(json.dumps(raw_diff, indent=2,))
    final_diff = raw_diff.replace(',', '').replace('"', '')
    return final_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration' +
                                                 ' files and shows a' +
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(generate_raw_diff(open_files(args.first_file),
                                          open_files(args.second_file))))


if __name__ == "__main__":
    main()
