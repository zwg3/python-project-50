#!/usr/bin/env python3
import argparse
from . import gendiff_yml
from . import gendiff_json
from . import gendata
from . import stylish_format
from . import plain_format
from . import json_format


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
        print(plain_format.plain(plain_format.same_deleter(gendata.generate_diff(files[0], files[1]))))
    elif args.format == "stylish" or "json":
        print(json_format.json_(gendata.generate_diff(files[0], files[1])))
    else:
        print(stylish_format.stylish(gendata.generate_diff(files[0], files[1])))


if __name__ == "__main__":
    main()
