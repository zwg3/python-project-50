import pytest
import os
from gendiff.formaters import stylish_format
from gendiff.formaters import plain_format
from gendiff import data_reader
from gendiff import diff_maker


@pytest.fixture
def correct_open():
    with open(os.path.abspath(
     'tests/fixtures/test_yml/diff_open.md')) as correct_result:
        correct_result = correct_result.read().rstrip('\n')
    return correct_result


@pytest.fixture
def correct_raw():
    with open(os.path.abspath(
     'tests/fixtures/test_yml/diff_result_raw.md')) as correct_result:
        correct_result = correct_result.read().rstrip('\n')
    return correct_result


@pytest.fixture
def correct_stylish():
    with open(
         'tests/fixtures/test_yml/diff_result_stylish.md') as correct_result:
        correct_result = correct_result.read().rstrip('\n')
    return correct_result


@pytest.fixture
def correct_plain():
    with open(
          'tests/fixtures/test_yml/diff_result_plain.md') as correct_result:
        correct_result = correct_result.read().rstrip('\n')
    return correct_result


@pytest.fixture
def open_file_output():
    return str(data_reader.file_opener(os.path.abspath(
        'tests/fixtures/test_yml/file3.yml')))


@pytest.fixture
def stylish_output():
    diff = diff_maker.make_diff((
     os.path.abspath('tests/fixtures/test_yml/file3.yml')),
     (os.path.abspath('tests/fixtures/test_yml/file4.yml')))
    stylish_diff = stylish_format.stylish(diff)
    return stylish_diff


@pytest.fixture
def raw_diff_output():
    raw_diff = diff_maker.make_diff((
        os.path.abspath('tests/fixtures/test_yml/file3.yml')),
        (os.path.abspath('tests/fixtures/test_yml/file4.yml')))
    return str(raw_diff)


@pytest.fixture
def plain_output():
    raw_diff = diff_maker.make_diff((
        os.path.abspath('tests/fixtures/test_yml/file3.yml')),
        (os.path.abspath('tests/fixtures/test_yml/file4.yml')))
    plain_diff = plain_format.plain(plain_format.same_deleter(raw_diff))
    return plain_diff


@pytest.mark.parametrize("result, correct_result", [
                                        ("open_file_output", "correct_open"),
                                        ("raw_diff_output", "correct_raw"),
                                        ("stylish_output", "correct_stylish"),
                                        ("plain_output", "correct_plain")
                                                   ])
def test_all(result, correct_result, request):
    result = request.getfixturevalue(result)
    correct_result = request.getfixturevalue(correct_result)
    assert result == correct_result
