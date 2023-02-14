import pytest
import os
from Gendiff.scripts import gendiff_json
from Gendiff.scripts import gendata
from Gendiff.scripts import stylish
from Gendiff.scripts import plain


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
    assert str(gendata.get_data(file_1, file_2)) == test_file


def test_stylish():
    file_1 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file3.json'))
    file_2 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file4.json'))
    raw = gendata.get_data(file_1, file_2)
    final_diff = stylish.stylish(raw)
    with open('tests/fixtures/test_json/diff_result_stylish.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff ==  test_file


def test_plain():
    file_1 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file3.json'))
    file_2 = gendiff_json.open_files(os.path.abspath('tests/fixtures/test_json/file4.json'))
    raw = gendata.get_data(file_1, file_2)
    final_diff = plain.plain(plain.same_deleter(raw))
    with open('tests/fixtures/test_json/diff_result_plain.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff ==  test_file
