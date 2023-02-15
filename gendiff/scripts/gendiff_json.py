#!/usr/bin/env python3
import json


def open_files(file_path):
    file = json.load(open(file_path))
    return file
