#!/usr/bin/env python3
from gendiff import gendiff
from gendiff import cli


def main():
    print(gendiff.generate_diff(*cli.get_arguments()))


if __name__ == "__main__":
    main()
