from json import loads
from .utils import get_file_content
from yaml import load


def get_json_diff(filepath1, filepath2):
    a = loads(get_file_content(filepath1))
    b = loads(get_file_content(filepath2))
    return get_diff_dict(a, b)


def get_yaml_diff(filepath1, filepath2):
    a = load(get_file_content(filepath1))
    b = load(get_file_content(filepath2))
    return get_diff_dict(a, b)


def get_differ(format):
    if format == "json":
        return get_yaml_diff
    elif format == "yml":
        return get_yaml_diff


def get_diff_dict(a, b):
    diff_a = set(a.keys()).difference(set(b.keys()))
    diff_b = set(b.keys()).difference(set(a.keys()))
    common = set(a.keys()).intersection(set(b.keys()))
    return {
        "dict_a": a,
        "dict_b": b,
        "diff_a_keys": diff_a,
        "diff_b_keys": diff_b,
        "common_keys": common,
    }
