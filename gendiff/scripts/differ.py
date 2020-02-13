from json import loads
from .utils import get_file_content
from yaml import load


def get_diff_summary(filepath1, filepath2, format="json"):
    if format == "json":
        a = loads(get_file_content(filepath1))
        b = loads(get_file_content(filepath2))
        print(a)
        print(b)
        diff_a = set(a.keys()).difference(set(b.keys()))
        diff_b = set(b.keys()).difference(set(a.keys()))
        common = set(a.keys()).intersection(set(b.keys()))
        return [a, b, diff_a, diff_b, common]
    else:
        a = load(get_file_content(filepath1))
        b = load(get_file_content(filepath2))
        print(a)
        print(b)
        diff_a = set(a.keys()).difference(set(b.keys()))
        diff_b = set(b.keys()).difference(set(a.keys()))
        common = set(a.keys()).intersection(set(b.keys()))
        return [a, b, diff_a, diff_b, common]


def diff_to_str(a, b, diff_a, diff_b, common, format="json"):
    if format == "json":
        result = "{"
        for key in common:
            if a[key] != b[key]:
                result += f"\n  - {key}: {a[key]}"
                result += f"\n  + {key}: {b[key]}"
            else:
                result += f"\n    {key}: {a[key]}"
        for key in diff_a:
            result += f"\n  - {key}: {a[key]}"
        for key in diff_b:
            result += f"\n  + {key}: {b[key]}"
        result += "\n}"
    return result
