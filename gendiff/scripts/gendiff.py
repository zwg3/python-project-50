#!/usr/bin/env python3
import argparse
import json
import copy


def open_files(file_path):
    file = json.load(open(file_path))
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


def main():
    parser = argparse.ArgumentParser(description=f'{"Compares "}'
                                                 f'{" two configuration"}'
                                                 f'{" files and shows a "}'
                                                 f'{" difference."}')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    raw_diff_existing = get_raw_diff_for_existing(open_files(args.first_file),
                                                  open_files(args.second_file))
    raw_diff_final = get_raw_diff_for_missing(open_files(args.first_file),
                                              open_files(args.second_file),
                                              raw_diff_existing)
    print(generate_diff(raw_diff_final))


if __name__ == "__main__":
    main()
