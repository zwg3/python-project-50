from . import data_reader


def file_prep(filepath):
    pattern = data_reader.file_opener(filepath)
    return pattern


def make_diff(pattern_1, pattern_2, formater=""):
    keys = set(list(pattern_1) + list(pattern_2))
    data_list = {}
    for i in dict.fromkeys(sorted(keys)):
        diff = {}
        if not (isinstance(pattern_1.get(i), dict)
           and isinstance(pattern_2.get(i), dict)):
            if i in pattern_1 and i in pattern_2:
                if pattern_1.get(i) == pattern_2.get(i):
                    diff["Key"] = i
                    diff["Type"] = "same"
                    diff["Value"] = pattern_2.get(i)
                    data_list[i] = diff
                else:
                    diff["Key"] = i
                    diff["Type"] = "changed"
                    diff["Value"] = pattern_1.get(i)
                    diff["Value_new"] = pattern_2.get(i)
                    data_list[i] = diff
            elif i not in pattern_2:
                diff["Key"] = i
                diff["Type"] = "removed"
                diff["Value"] = pattern_1.get(i)
                data_list[i] = diff
            else:
                diff["Key"] = i
                diff["Type"] = "added"
                diff["Value"] = pattern_2.get(i)
                data_list[i] = diff
        else:
            diff["Key"] = i
            diff["Type"] = "parent"
            diff["Value"] = make_diff(pattern_1[i], pattern_2[i])
            data_list[i] = diff
    return data_list
