#!/usr/bin/env python3

def generate_diff(first, second):
    ss = set(list(first) + list(second))
    data_list = {}
    for i in dict.fromkeys(sorted(ss)):
        diff = {}
        if not (type(first.get(i)) == dict and type(second.get(i)) == dict):
            if i in first and i in second:
                if first.get(i) == second.get(i):
                    diff["Key"] = i
                    diff["Type"] = "same"
                    diff["Value"] = second.get(i)
                    data_list[i] = diff
                else:
                    diff["Key"] = i
                    diff["Type"] = "changed"
                    diff["Value"] = first.get(i)
                    diff["Value_new"] = second.get(i)
                    data_list[i] = diff
            elif i not in second:
                diff["Key"] = i
                diff["Type"] = "removed"
                diff["Value"] = first.get(i)
                data_list[i] = diff
            else:
                diff["Key"] = i
                diff["Type"] = "added"
                diff["Value"] = second.get(i)
                data_list[i] = diff
        else:
            diff["Key"] = i
            diff["Type"] = "parent"
            diff["Value"] = generate_diff(first[i], second[i])
            data_list[i] = diff
    return data_list
