import pytest
import os
import sys
#sys.path.append(f'{os.getcwd()}/')
from gendiff.scripts import gendiff_json
from gendiff.scripts import gendata
from gendiff.scripts import stylish_format
from gendiff.scripts import plain_format


@pytest.fixture
def open_file_1():
    return gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file3.json'))


def test_open(open_file_1):
    with open(os.path.abspath('tests/fixtures/test_json/diff_open.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(open_file_1) == test_file


def test_gen_raw():
    file_1 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file3.json'))
    file_2 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file4.json'))
    with open(os.path.abspath('tests/fixtures/test_json/diff_result_raw.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(gendata.generate_diff(file_1, file_2)) == test_file


def test_stylish():
    file_1 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file3.json'))
    file_2 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file4.json'))
    raw = gendata.generate_diff(file_1, file_2)
    final_diff = stylish_format.stylish(raw)
    with open('tests/fixtures/test_json/diff_result_stylish.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff ==  test_file


def test_plain():
    file_1 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file3.json'))
    file_2 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file4.json'))
    raw = gendata.generate_diff(file_1, file_2)
    final_diff = plain_format.plain(plain_format.same_deleter(raw))
    with open('tests/fixtures/test_json/diff_result_plain.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff ==  test_file
