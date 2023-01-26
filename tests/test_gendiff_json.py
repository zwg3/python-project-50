import pytest
import os
from gendiff.scripts import gendiff_json


@pytest.fixture
def open_file_1():
    return gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file1.json'))


def test_open(open_file_1):
    with open(os.path.abspath('tests/fixtures/test_json/open_result.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(open_file_1) == test_file


def test_gen_raw_existing():
    file_1 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file1.json'))
    file_2 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file2.json'))
    with open(os.path.abspath('tests/fixtures/test_json/diff_result_raw_existing.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(gendiff_json.get_raw_diff_for_existing(file_1, file_2)) == test_file


def test_gen_raw_missing():
    file_1 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file1.json'))
    file_2 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file2.json'))
    raw_existing = gendiff_json.get_raw_diff_for_existing(file_1, file_2)
    with open(os.path.abspath('tests/fixtures/test_json/diff_result_raw_missing.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(gendiff_json.get_raw_diff_for_missing(file_1, file_2, raw_existing)) == test_file


def test_final_diff():
    file_1 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file1.json'))
    file_2 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file2.json'))
    raw_existing = gendiff_json.get_raw_diff_for_existing(file_1, file_2)
    raw_missing = gendiff_json.get_raw_diff_for_missing(file_1, file_2, raw_existing)
    final_diff = gendiff_json.generate_diff(raw_missing)
    with open('tests/fixtures/test_json/diff_result_final.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff ==  test_file
