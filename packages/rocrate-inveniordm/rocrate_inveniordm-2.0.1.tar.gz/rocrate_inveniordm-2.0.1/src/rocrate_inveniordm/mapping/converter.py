import json
import sys
from importlib import resources
import rocrate_inveniordm.mapping as mapping

import rocrate_inveniordm.mapping.condition_functions as cf
import rocrate_inveniordm.mapping.processing_functions as pf


def main():
    """
    For test purposes only.
    """
    if len(sys.argv) != 2:
        print("Usage: python converter.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace(".rc.json", ".dc.json")
    f = open(input_file)
    rc = json.load(f)

    output = convert(rc)

    with open(output_file, "w") as outfile:
        json.dump(output, outfile, indent=4)

    return


def get_arrays_from_from_values(input_list):
    output_set = set()
    for string in input_list:
        delimiter_index = string.rfind("[]")
        if delimiter_index != -1:
            processed_string = string[
                : delimiter_index + 2
            ]  # Include the "[]" in the output
            output_set.add(processed_string)
    output_list = list(output_set)
    return output_list


def load_mapping_json() -> dict:
    mapping_file = resources.files(mapping) / "mapping.json"
    with mapping_file.open("r") as f:
        mapping_json = json.load(f)
    return mapping_json


def convert(rc, metadata_only=False):
    """
    Convert a RO-Crate to a DataCite object

    :param rc: The RO-Crate
    :param metadata_only: Whether it is a metadata-only DataCite
    """

    m = load_mapping_json()

    dc = setup_dc()
    if metadata_only:
        dc["files"]["enabled"] = False
    print(dc)

    root_rules = m.get("$root")

    for mapping_class in root_rules:
        print()

        # Ignore mappings that are marked as ignored
        if "_ignore" in root_rules.get(mapping_class).keys():
            print(f"|x Ignoring {mapping_class}")
            continue

        print(f"|- Applying rule collection {mapping_class}")

        root_mappings = root_rules.get(mapping_class)

        mappings = root_mappings.get("mappings")

        mapping_paths = get_mapping_paths(rc, mappings)

        print(f"\t\t|- Paths: {mapping_paths}")

        is_any_present = False

        for mapping_key in mappings:
            print(f"\t|- Applying mapping {mapping_key}")

            mapping = mappings.get(mapping_key)
            dc, any_present = apply_mapping(mapping, mapping_paths, rc, dc)
            is_any_present = is_any_present or any_present

        if not is_any_present:
            none_present_value = root_mappings.get("ifNonePresent")
            if none_present_value is not None:
                print(f"\t|- Applying ifNonePresent rule {none_present_value}")
                for none_present_key in none_present_value:
                    none_present_mapping_value = none_present_value.get(
                        none_present_key
                    )
                    dc = set_dc(dc, none_present_key, none_present_mapping_value)

    return dc


def get_mapping_paths(rc, mappings):
    # retrieve all array values
    all_from_values = []
    for key in mappings:
        mapping = mappings.get(key)
        from_value = mapping.get("from")
        if from_value is not None:
            all_from_values.append(from_value)

    array_values = get_arrays_from_from_values(all_from_values)

    # Extract all possible paths (used for arrays)
    mapping_paths = {}
    for i in array_values:
        mapping_paths[i] = get_paths(rc, i)

    return mapping_paths


def apply_mapping(mapping, mapping_paths, rc, dc):
    rule_applied = False

    if "_ignore" in mapping.keys():
        return dc, rule_applied

    from_mapping_value = mapping.get("from")
    to_mapping_value = mapping.get("to")
    value_mapping_value = mapping.get("value")
    processing_mapping_value = mapping.get("processing")
    only_if_value = mapping.get("onlyIf")

    # The following steps are performed:
    # 1. Get the value from the RO-Crate (from)
    # 2. Check if the rule should be applied (onlyIf)
    # 3. Process the value (processing)
    # 4. Put the value into the correct format (value)
    # 5. Add the value to the DataCite object (to)

    # Get the correct mapping paths. change this. now it is overriden
    paths = [[]]

    if from_mapping_value:
        delimiter_index = from_mapping_value.rfind("[]")
    else:
        delimiter_index = -1

    if delimiter_index != -1:
        processed_string = from_mapping_value[: delimiter_index + 2]
        paths = mapping_paths.get(processed_string)
        print(f"\t\t|- Paths: {paths}")

    for path in paths:
        print(f"PATH: {path}")
        new_path = path.copy()
        from_value = get_rc(rc.copy(), from_mapping_value, new_path)

        # if (from_value is None):
        #    continue

        if only_if_value is not None:
            print(f"\t\t|- Checking condition {only_if_value}")
            if not check_condition(only_if_value, from_value):
                return dc, rule_applied

        if processing_mapping_value:
            from_value = process(processing_mapping_value, from_value)

        if value_mapping_value:
            from_value = transform_to_target_format(value_mapping_value, from_value)

        if from_value is not None:
            print(
                f"\t\t|- Adding {from_value} to {to_mapping_value} with path {path.copy()}"
            )
            rule_applied = True
            print(dc, to_mapping_value, from_value)
            dc = set_dc(dc, to_mapping_value, from_value, path.copy())

    return dc, rule_applied


def get_paths(rc, key):
    """
    Get all possible paths for a given key

    :param rc: The RO-Crate
    :param key: The key to get the paths for
    """
    print(f"\t\t|- Getting paths for {key}")
    keys = key.split(".")
    temp = rc_get_rde(rc)
    paths = []
    get_paths_recursive(rc, temp, keys, paths, [])
    print(f"\t\t\t|- Found paths {paths}")
    return paths


def get_paths_recursive(rc, temp, keys, paths, path):

    if len(keys) == 0:
        paths.append(path)
        return

    current_key = keys[0]

    # clean key
    cleaned_key = current_key
    cleaned_key = cleaned_key.replace("[]", "").replace("$", "")
    if temp is None:
        return
    if cleaned_key not in temp.keys():
        return

    if current_key.endswith("[]"):
        new_current_key = current_key
        if current_key.startswith("$"):
            new_current_key = current_key[1:]
        if isinstance(temp[new_current_key[:-2]], list):
            for i in range(len(temp[new_current_key[:-2]])):
                new_path = path.copy()
                new_path.append(i)
                if current_key.startswith("$"):
                    new_temp = get_rc_ref(rc, temp, current_key[:-2], i)
                else:
                    new_temp = temp[new_current_key[:-2]][i]

                get_paths_recursive(rc, new_temp, keys[1:], paths, new_path)
        else:
            new_path = path.copy()
            new_path.append(-1)
            if current_key.startswith("$"):
                new_temp = get_rc_ref(rc, temp, current_key[:-2])
            else:
                new_temp = temp[current_key[:-2]]

            get_paths_recursive(rc, new_temp, keys[1:], paths, new_path)
    else:
        if current_key == "$":
            temp = get_rc_ref(rc, temp, current_key)
        else:
            temp = temp[current_key]
        get_paths_recursive(rc, temp, keys[1:], paths, path)

    return


def rc_get_rde(rc):
    """
    Retrieves the Root Date Entity from the given RO-Crate.

    :param rc: The RO-Crate to retrieve the RDE from.
    :return: The Root Data Entity of the given RO-Crate.
    """

    # Following the RO-Crate specification (https://www.researchobject.org/ro-crate/1.1/root-data-entity.html),
    # use the following algorithm to find the RDE:
    #
    # For each entity in @graph array
    #   if the conformsTo property is a URI that starts with https://w3id.org/ro/crate/
    #       from this entity's about object keep the @id URI as variable root
    # For each entity in @graph array
    #   if the entity has an @id URI that matches the root return it

    root = None
    graph = rc.get("@graph")
    for entity in graph:
        conformsTo = entity.get("conformsTo")
        if (
            conformsTo
            and conformsTo.get("@id")
            and conformsTo.get("@id").startswith("https://w3id.org/ro/crate/")
        ):
            root = entity.get("about").get("@id")

    for entity in graph:
        if entity.get("@id") == root:
            return entity


def contains_atatthis(value):
    """
    Checks if the given value contains the string "@@this".
    The value can be a string or a dictionary.

    :param value: The value to check.
    :return: True if the value contains "@@this", False otherwise.
    """
    if isinstance(value, str):
        return "@@this" in value
    elif isinstance(value, dict):
        for key, v in value.items():
            if isinstance(v, str):
                if "@@this" in v:
                    return True
            else:
                return contains_atatthis(value[key])

    return False


def transform_to_target_format(format, value):
    """
    Transforms the given value to the given format.
    The format parameter is a string, which can contain the following special values:
        - @@this: The value of the key itself

    :param format: The format to apply to the value.
    :param value: The value to format.
    :return: The formatted value.
    """
    if format is not None:
        if value:
            print(f"\t\t|- Formatting value {value} according to {format}.")
            format = format_value(format, value)
            return format
        elif value is None and contains_atatthis(format):
            format = None
            return format
        print(f"\t\t|- Formatted value {value} is {format}")
    return format


def get_rc(rc, from_key, path=[]):
    """
    Retrieves the value of the given key from the given RO-Crate.
    A key consists of multiple subkeys, separated by a dot (.).
    If a subkey starts with a $, then it is a reference to another key.

    :param rc: The RO-Crate to retrieve the value from.
    :param from_key: The key to retrieve the value from.
    :return: The value of the given key in the given RO-Crate.
    """
    result = None

    if not from_key:
        return None

    print(f"\t\t|- Retrieving value {from_key} with path {path} from RO-Crate.")
    keys = from_key.split(".")
    print(keys)
    temp = rc_get_rde(rc)

    for key in keys:
        cleaned_key = key.replace("[]", "").replace("$", "")
        print(f"\t\t|- Cleaned key: {cleaned_key}")
        if key.startswith("$"):
            # we need to dereference the key
            index = None
            if key.endswith("[]"):
                index = path[0]
                path = path[1:]
                if index == -1:
                    temp = get_rc_ref(rc, temp, "$" + cleaned_key)
                else:
                    temp = get_rc_ref(rc, temp, "$" + cleaned_key, index)
            else:
                temp = get_rc_ref(rc, temp, "$" + cleaned_key)

            if temp is None:
                return None

        elif cleaned_key not in temp.keys():
            # The key could not be found in the RO-Crate
            return None

        else:
            if key.endswith("[]"):
                index = path[0]
                path = path[1:]
                if index == -1:
                    temp = temp.get(cleaned_key)
                else:
                    temp = temp.get(cleaned_key)[index]
            else:
                temp = temp.get(cleaned_key)

    result = temp

    print(f"\t\t|- Value for key {from_key} is {result}")

    if result and isinstance(result, dict):
        # If the value is a JSON object, then we ignore the rule (since another rule must be implemented on how to handle it)
        return None

    return result


def get_rc_ref(rc, parent, from_key, index=None):
    """
    Retrieves the entity referenced by the given $-prefixed key from the given RO-Crate.

    Example: Calling get_rc_ref(rc, parent, "$affiliation") on the following RO-Crate

    rc: {
        ...
        {
            "@id": "https://orcid.org/0000-0002-8367-6908",
            "@type": "Person",
            "name": "J. Xuan"
            "affiliation": {"@id": "https:/abc"}
        }
        {
            "@id": "https:/abc",
            "@type": "Organization",
            "name": "ABC University"
        }
    }

    parent: {
            "@id": "https://orcid.org/0000-0002-8367-6908",
            "@type": "Person",
            "name": "J. Xuan"
            "affiliation": {"@id": "https:/abc"}
        }

    returns {
            "@id": "https:/abc",
            "@type": "Organization",
            "name": "ABC University"
        }
    """
    print(f"\t\t|- Retrieving referenced entity {from_key} from RO-Crate.")
    if from_key and not from_key.startswith("$"):
        raise Exception(f"$-prefixed key expected, but {from_key} found.")
    id_val = parent.get(from_key[1:])
    if isinstance(id_val, list):
        id_val = id_val[index]
    if isinstance(id_val, dict):
        id = id_val.get("@id")
        print(f"\t\t\t|- Id is {id}")
    else:
        return None

    for entity in rc.get("@graph"):
        if entity.get("@id") == id:
            print(f"\t\t\t|- Found entity {entity}")
            return entity

    return None


def get_rc_ref_root(rc, from_key):
    """
    Retrieves the entity referenced by the given $-prefixed key from the given RO-Crate.

    :param rc: The RO-Crate to retrieve the referenced entity from.
    :param from_key: The $-prefixed key to retrieve the referenced entity from.
    :return: The referenced entity of the given RO-Crate.
    """
    print(f"\t\t|- Retrieving referenced entity {from_key} from RO-Crate.")
    if from_key and not from_key.startswith("$"):
        raise Exception(f"$-prefixed key expected, but {from_key} found.")

    keys = from_key.split(".")
    root = rc_get_rde(rc)
    if root.get(keys[0][1:]) is None:
        print(f"\t\t|- Key {keys[0]} not found in RO-Crate.")
        return None
    target_entity_id = root.get(keys[0][1:]).get("@id")
    target_entity = None

    for entity in rc.get("@graph"):
        if entity.get("@id") == target_entity_id:
            target_entity = entity
            break
    return target_entity


def format_value(format, value):
    """
    Formats the given value according to the given format.
    The format can be a string or a dictionary.
    If the format is a string, the value is inserted at the position of @@this.
    If the format is a dictionary, the value is inserted at the position of @@this in each value of the dictionary.

    For example, if the format is {"a": "@@this", "b": "c"}, and the value is "d", the result is {"a": "d", "b": "c"}.

    :param format: The format to use.
    :param value: The value to insert.
    :return: The formatted value.
    """
    if isinstance(format, str):
        return format.replace("@@this", value)
    elif isinstance(format, dict):
        # format = {}
        for key, v in format.items():
            format[key] = format_value(v, value)
        return format
    elif isinstance(format, bool):
        return format
    else:

        raise TypeError(
            f"Format must be a string, dictionary, or bool, but is {type(format)}."
        )


def set_dc(dictionary, key, value=None, path=[]):
    """
    Sets the value of the given key in the given dictionary to the given value.
    If the key does not exist, it is created.
    If the key ends with "[]", the value is appended to the list of values for the key.

    :param dictionary: The dictionary to set the value in.
    :param key: The key to set the value for.
    :param value: The value to set.
    :param path: The path to the key.
    """
    keys = key.split(".")
    current_dict = dictionary
    index = -1
    for key_part in keys:
        print(f"\t\t\t|- Key part: {key_part}")
        if len(path) > 0:
            index = path[0]
        else:
            index = 0
        if key_part.endswith("[]") and not key_part[:-2] in current_dict:
            path = path[1:]
            current_dict[key_part[:-2]] = [{}]
            last_val = current_dict[key_part[:-2]]
            current_dict = current_dict[key_part[:-2]][
                0
            ]  # index is 0 here (if we assume that paths is in ascending order)

        elif key_part.endswith("[]") and key_part[:-2] in current_dict:
            path = path[1:]
            last_val = current_dict[key_part[:-2]]

            if len(current_dict[key_part[:-2]]) <= index:
                current_dict[key_part[:-2]].append({})

            current_dict = current_dict[key_part[:-2]][index]

        elif key_part not in current_dict and not key_part.endswith("[]"):
            last_val = current_dict
            current_dict[key_part] = {}
            current_dict = current_dict[key_part]

        else:
            last_val = current_dict
            current_dict = current_dict[key_part]

    last_key = keys[-1]
    if last_key.endswith("[]"):
        last_val[index] = value
    else:
        last_val[last_key] = value
    return dictionary


def check_condition(condition_rule, value):
    """
    Checks if a value matches a condition rule.
    The condition rule is a string that starts with ? and is followed by the name of the function to apply.
    The function must be defined in condition_functions.py.

    :param condition_rule: The condition rule to apply.
    :param value: The value to check.
    :return: True if the value matches the condition, False otherwise.
    """
    if not condition_rule.startswith("?"):
        raise ValueError(f"Condition rule {condition_rule} must start with ?")
    try:
        function = getattr(cf, condition_rule[1:])
    except AttributeError:
        raise NotImplementedError(f"Function {condition_rule} not implemented.")
    return function(value)


def process(process_rule, value):
    """
    Processes a value according to a processing rule.
    The processing rule is a string that starts with $ and is followed by the name of the function to apply.
    The function must be defined in processing_functions.py.

    :param process_rule: The processing rule to apply.
    :param value: The value to process.
    :return: The processed value.
    """
    if not process_rule.startswith("$"):
        raise ValueError(f"Processing rule {process_rule} must start with $")
    try:
        function = getattr(pf, process_rule[1:])
    except AttributeError:
        raise NotImplementedError(f"Function {process_rule} not implemented.")
    return function(value)


def setup_dc():
    # https://inveniordm.docs.cern.ch/reference/metadata/#metadata
    dc = {
        "access": {
            "record": "public",  # public or restricted; 1
            "files": "public",  # public or restricted; 1
            "embargo": {"active": False},  # 0-1
        },
        "metadata": {},
        "files": {"enabled": True},
    }
    return dc


if __name__ == "__main__":
    main()
