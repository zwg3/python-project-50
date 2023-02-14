#!/usr/bin/env python3
import argparse
from . import gendiff_yml
from . import gendiff_json
from . import gendata
from . import stylish
from . import plain


def main():
    parser = argparse.ArgumentParser(description=f'{"Compares "}'
                                                 f'{" two configuration"}'
                                                 f'{" files and shows a "}'
                                                 f'{" difference."}')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output', default=stylish)
    args = parser.parse_args()
    if args.format == "plain":
        if str(args.first_file).endswith('.json'):
            print(plain.plain(gendata.get_data(gendiff_json.open_files(
                args.first_file), gendiff_json.open_files(args.second_file))))
        elif str(args.first_file).endswith('.yml') or (str(
                args.first_file).endswith('.yaml')):
            print(plain.plain(gendata.get_data(gendiff_yml.open_files(
                args.first_file), gendiff_yml.open_files(args.second_file))))
    else:
        if str(args.first_file).endswith('.json'):
            print(stylish.stylish(gendata.get_data(gendiff_json.open_files(
                args.first_file), gendiff_json.open_files(args.second_file))))
        elif str(args.first_file).endswith('.yml') or (str(
                args.first_file).endswith('.yaml')):
            print(stylish.stylish(gendata.get_data(gendiff_yml.open_files(
                args.first_file), gendiff_yml.open_files(args.second_file))))


if __name__ == "__main__":
    main()
