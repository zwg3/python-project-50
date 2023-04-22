from . import diff_maker
from .formaters import stylish_format
from .formaters import plain_format
from .formaters import json_format


def generate_diff(filepath1, filepath2, format_type="stylish"):
    pattern_1 = diff_maker.file_prep(filepath1)
    pattern_2 = diff_maker.file_prep(filepath2)
    raw_data = diff_maker.make_diff(pattern_1, pattern_2, format_type)
    if format_type == "plain":
        return (plain_format.plain(
                plain_format.same_deleter(raw_data)))
    elif format_type == "json":
        return (json_format.json_(raw_data))
    elif format_type == "stylish":
        return (stylish_format.stylish(raw_data))
    else:
        raise Exception('Please use the following options only: \
"stylish", "json"  or "plain".')
