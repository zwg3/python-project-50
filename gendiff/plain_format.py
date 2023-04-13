import json


def same_deleter(raw_data):
    for i in raw_data.copy():
        if raw_data[i]["Type"] != "parent":
            if raw_data[i]["Type"] == "same":
                del raw_data[i]
        else:
            same_deleter(raw_data[i]["Value"])
    return raw_data


def plain_formater_simple(property, parent=''):
    start_string = 'Property '
    parent_string = ""
    if parent:
        parent_string = f'{parent}.'
    if property["Type"] == "removed":
        return f"{start_string}'{parent_string}{property['Key']}' was removed"
    elif property["Type"] == "same":
        return f"{start_string}'{parent_string}{property['Key']}' is the same"
    elif property["Type"] == "added":
        if isinstance(property['Value'], dict):
            return (f"{start_string}'{parent_string}{property['Key']}'"
                    f" was added with value: [complex value]")
        else:
            return (f"{start_string}'{parent_string}{property['Key']}'"
                    f" was added with value: {json.dumps(property['Value'])}")


def plain_formater_complex(property, parent=''):
    start_string = 'Property '
    parent_string = ""
    if parent:
        parent_string = f'{parent}.'
    if isinstance(property['Value'], dict):
        return (f"{start_string}'{parent_string}{property['Key']}'"
                f" was updated."
                f" From [complex value] to {json.dumps(property['Value_new'])}")
    elif isinstance(property['Value_new'], dict):
        return (f"{start_string}'{parent_string}{property['Key']}'"
                f" was updated."
                f" From {json.dumps(property['Value'])} to [complex value]")
    else:
        if parent_string:
            return (f"{start_string}'{parent_string}{property['Key']}'"
                    f" was updated."
                    f" From {json.dumps(property['Value'])}"
                    f" to {json.dumps(property['Value_new'])}")
        else:
            return (f"{start_string}'{property['Key']}'"
                    f" was updated."
                    f" From {json.dumps(property['Value'])}"
                    f" to {json.dumps(property['Value_new'])}")


def plain(raw_data, parent=False):
    string_plain = []
    for i in raw_data:
        if raw_data[i]["Type"] == "parent":
            if parent:
                parent_new = parent + "." + raw_data[i]["Key"]
                temp_string = []
                temp_line = plain(raw_data[i]["Value"], parent=parent_new)
                temp_string.append(temp_line)
                string_plain.append(temp_string)
            else:
                temp_string = []
                temp_line = plain(raw_data[i]["Value"], parent=i)
                temp_string.append(temp_line)
                string_plain.append(temp_string)
        elif raw_data[i]["Type"] != "changed":
            temp_string = []
            temp_string.append(
                plain_formater_simple(raw_data[i], parent=parent))
            string_plain.append(temp_string)
        else:
            temp_string = []
            temp_string.append(
                plain_formater_complex(raw_data[i], parent=parent))
            string_plain.append(temp_string)
    string_plain = ["".join(x) for x in string_plain]
    string_plain = [i.replace('"', "'") for i in string_plain]
    string_plain = "\n".join(string_plain)
    return string_plain
