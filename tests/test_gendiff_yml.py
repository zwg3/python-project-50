import pytest
import os
from gendiff import gendiff_yml
from gendiff import gendiff
from gendiff import stylish_format
from gendiff import plain_format

@pytest.fixture
def open_file_1():
    return gendiff_yml.open_files(os.path.abspath('tests/fixtures/test_yml/file3.yml'))


def test_open(open_file_1):
    with open(os.path.abspath('tests/fixtures/test_yml/diff_open.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(open_file_1) == test_file


def test_gen_raw():
    file_1 = gendiff_yml.open_files(os.path.abspath('tests/fixtures/test_yml/file3.yml'))
    file_2 = gendiff_yml.open_files(os.path.abspath('tests/fixtures/test_yml/file4.yml'))
    with open(os.path.abspath('tests/fixtures/test_yml/diff_result_raw.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(gendiff.generate_diff(file_1, file_2)) == test_file


def test_stylish():
    file_1 = gendiff_yml.open_files(os.path.abspath('tests/fixtures/test_yml/file3.yml'))
    file_2 = gendiff_yml.open_files(os.path.abspath('tests/fixtures/test_yml/file4.yml'))
    raw = gendiff.generate_diff(file_1, file_2)
    final_diff = stylish_format.stylish(raw)
    with open('tests/fixtures/test_yml/diff_result_stylish.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff ==  test_file


def test_plain():
    file_1 = gendiff_yml.open_files(os.path.abspath('tests/fixtures/test_yml/file3.yml'))
    file_2 = gendiff_yml.open_files(os.path.abspath('tests/fixtures/test_yml/file4.yml'))
    raw = gendiff.generate_diff(file_1, file_2)
    final_diff = plain_format.plain(plain_format.same_deleter(raw))
    with open('tests/fixtures/test_yml/diff_result_plain.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff ==  test_file
    