import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description=f'{"Compares "}'
                                                 f'{" two configuration"}'
                                                 f'{" files and shows a "}'
                                                 f'{" difference."}')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', nargs='?',
                        help='set format of output', default='stylish')
    args = parser.parse_args()
    filepath1 = args.first_file
    filepath2 = args.second_file
    formater = args.format
    return filepath1, filepath2, formater
