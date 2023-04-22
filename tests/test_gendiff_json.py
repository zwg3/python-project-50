import pytest
import os
from gendiff import data_reader
from gendiff import diff_maker
from gendiff import gendiff


@pytest.fixture
def correct_open():
    with open(os.path.abspath(
            'tests/fixtures/test_json/diff_open.md')) as correct_res:
        correct_res = correct_res.read().rstrip('\n')
    return correct_res


@pytest.fixture
def correct_raw():
    with open(os.path.abspath(
            'tests/fixtures/test_json/diff_result_raw.md')) as correct_res:
        correct_res = correct_res.read().rstrip('\n')
    return correct_res


@pytest.fixture
def correct_stylish():
    with open(
            'tests/fixtures/test_json/diff_result_stylish.md') as correct_res:
        correct_res = correct_res.read().rstrip('\n')
    return correct_res


@pytest.fixture
def correct_plain():
    with open(
            'tests/fixtures/test_json/diff_result_plain.md') as correct_res:
        correct_res = correct_res.read().rstrip('\n')
    return correct_res


@pytest.fixture
def open_file_output():
    return str(data_reader.file_opener(os.path.abspath(
        'tests/fixtures/test_json/file3.json')))


@pytest.fixture
def stylish_output():
    stylish_diff = gendiff.generate_diff((
        os.path.abspath('tests/fixtures/test_json/file3.json')),
        (os.path.abspath('tests/fixtures/test_json/file4.json')))
    return stylish_diff


@pytest.fixture
def raw_diff_output():
    raw_diff = diff_maker.make_diff((diff_maker.file_prep(
        os.path.abspath('tests/fixtures/test_json/file3.json'))),
        diff_maker.file_prep(
        (os.path.abspath('tests/fixtures/test_json/file4.json'))))
    return str(raw_diff)


@pytest.fixture
def plain_output():
    plain_diff = gendiff.generate_diff((
        os.path.abspath('tests/fixtures/test_json/file3.json')),
        (os.path.abspath('tests/fixtures/test_json/file4.json')),
        format_type='plain')
    return plain_diff


@pytest.mark.parametrize("result, correct_res",
                         [
                             ("open_file_output", "correct_open"),
                             ("raw_diff_output", "correct_raw"),
                             ("stylish_output", "correct_stylish"),
                             ("plain_output", "correct_plain")
                         ])
def test_all(result, correct_res, request):
    result = request.getfixturevalue(result)
    correct_res = request.getfixturevalue(correct_res)
    assert result == correct_res
