import pytest
import os
from gendiff.scripts import gendiff


@pytest.fixture
def open_file_1():
    return gendiff.open_files(os.path.abspath('tests/fixtures/file1.json'))


def test_open(open_file_1):
    with open(os.path.abspath('tests/fixtures/open_result.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(open_file_1) == test_file


def test_gen_raw():
    file_1 = gendiff.open_files(os.path.abspath('tests/fixtures/file1.json'))
    file_2 = gendiff.open_files(os.path.abspath('tests/fixtures/file2.json'))
    with open(os.path.abspath('tests/fixtures/diff_result_raw.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(gendiff.generate_raw_diff(file_1, file_2)) == test_file


def test_final_diff():
    file_1 = gendiff.open_files(os.path.abspath('tests/fixtures/file1.json'))
    file_2 = gendiff.open_files(os.path.abspath('tests/fixtures/file2.json'))
    raw = gendiff.generate_raw_diff(file_1, file_2)
    diff = gendiff.generate_diff(raw)
    with open('tests/fixtures/diff_result_final.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert diff ==  test_file
