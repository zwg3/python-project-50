import argparse
from .import gendiff_json
from . import gendiff_yml


def main():
    parser = argparse.ArgumentParser(description=f'{"Compares "}'
                                                 f'{" two configuration"}'
                                                 f'{" files and shows a "}'
                                                 f'{" difference."}')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    if str(args.first_file).endswith('.json'):
        raw_diff_existing = gendiff_json.get_raw_diff_for_existing(
            gendiff_json.open_files(args.first_file),
            gendiff_json.open_files(args.second_file))
        raw_diff_final = gendiff_json.get_raw_diff_for_missing(
            gendiff_json.open_files(args.first_file),
            gendiff_json.open_files(args.second_file), raw_diff_existing)
        print(gendiff_json.generate_diff(raw_diff_final))
    elif str(args.first_file).endswith('.yml') or (str(
            args.first_file).endswith('.yaml')):
        raw_diff_existing = gendiff_yml.get_raw_diff_for_existing(
            gendiff_yml.open_files(args.first_file),
            gendiff_yml.open_files(args.second_file))
        raw_diff_final = gendiff_yml.get_raw_diff_for_missing(
            gendiff_yml.open_files(args.first_file),
            gendiff_yml.open_files(args.second_file), raw_diff_existing)
        print(gendiff_yml.generate_diff(raw_diff_final))


if __name__ == "__main__":
    main()
