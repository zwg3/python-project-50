#!/usr/bin/env python3
import yaml


def open_files(file_path):
    file = yaml.load(open(file_path), Loader=yaml.FullLoader)
    return file
