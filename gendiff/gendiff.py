from . import diff_maker
from .formaters import stylish_format
from .formaters import plain_format
from .formaters import json_format


def generate_diff(filepath1, filepath2, format_type="stylish"):
    if format_type == "plain":
        return (plain_format.plain(
                plain_format.same_deleter(
                    diff_maker.make_diff(filepath1, filepath2, format_type))))
    elif format_type == "json":
        return (json_format.json_(
            diff_maker.make_diff(
                filepath1, filepath2, format_type)))
    elif format_type != "stylish_format" or "stylish":
        raise Exception('Incorrect fomat type.'
                        'The available formaters are:'
                        ' "plain", "stylish" and "json".')
    else:
        return (stylish_format.stylish(
            diff_maker.make_diff(filepath1, filepath2, format_type)))
