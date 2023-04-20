import pytest
import os
from gendiff.formaters import stylish_format
from gendiff.formaters import plain_format
from gendiff import data_reader
from gendiff import diff_maker


@pytest.fixture
def open_file_1():
    return data_reader.file_opener(os.path.abspath(
        'tests/fixtures/test_yml/file3.yml'))


def test_open(open_file_1):
    with open(os.path.abspath(
            'tests/fixtures/test_yml/diff_open.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(open_file_1) == test_file


def test_gen_raw():
    files = diff_maker.make_diff((
        os.path.abspath('tests/fixtures/test_yml/file3.yml')),
        (os.path.abspath('tests/fixtures/test_yml/file4.yml')))
    with open(os.path.abspath(
            'tests/fixtures/test_yml/diff_result_raw.md')) as test_file:
        test_file = test_file.read().rstrip('\n')
    assert str(files) == test_file


def test_stylish():
    raw = diff_maker.make_diff((
        os.path.abspath('tests/fixtures/test_yml/file3.yml')),
        (os.path.abspath('tests/fixtures/test_yml/file4.yml')))
    final_diff = stylish_format.stylish(raw)
    with open('tests/fixtures/test_yml/diff_result_stylish.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff == test_file


def test_plain():
    raw = diff_maker.make_diff((
        os.path.abspath('tests/fixtures/test_yml/file3.yml')),
        (os.path.abspath('tests/fixtures/test_yml/file4.yml')))
    final_diff = plain_format.plain(plain_format.same_deleter(raw))
    with open('tests/fixtures/test_yml/diff_result_plain.md') as test_file:
        test_file = test_file.read().rstrip('\n')
    assert final_diff == test_file
