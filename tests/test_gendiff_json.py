import pytest
import os
from gendiff import stylish_format
from gendiff import plain_format
from gendiff import gendiff


@pytest.fixture
def open_file_1():
    return gendiff.open_files(os.path.abspath(
        'tests/fixtures/test_json/file3.json'))


def test_open(open_file_1):
    with open(os.path.abspath(
            'tests/fixtures/test_json/diff_open.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(open_file_1) == test_file


def test_gen_raw():
    files = gendiff.get_data(gendiff.open_files(
        os.path.abspath('tests/fixtures/test_json/file3.json')),
        (os.path.abspath('tests/fixtures/test_json/file4.json')))
    with open(os.path.abspath(
            'tests/fixtures/test_json/diff_result_raw.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(files) == test_file


def test_stylish():
    raw = gendiff.get_data(gendiff.open_files(
        os.path.abspath('tests/fixtures/test_json/file3.json')),
        (os.path.abspath('tests/fixtures/test_json/file4.json')))
    final_diff = stylish_format.stylish(raw)
    with open('tests/fixtures/test_json/diff_result_stylish.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff == test_file


def test_plain():
    raw = gendiff.get_data(gendiff.open_files(
        os.path.abspath('tests/fixtures/test_json/file3.json')),
        (os.path.abspath('tests/fixtures/test_json/file4.json')))
    final_diff = plain_format.plain(plain_format.same_deleter(raw))
    with open('tests/fixtures/test_json/diff_result_plain.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff == test_file
