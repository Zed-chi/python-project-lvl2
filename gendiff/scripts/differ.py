from json import loads
from .utils import get_file_content


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


def print_diff(a, b, diff_a, diff_b, common, format="json"):
    if format == "json":
        print("{")
        for key in common:
            if a[key] != b[key]:
                print(f"  - {key}: {a[key]}")
                print(f"  + {key}: {b[key]}")
            else:
                print(f"    {key}: {a[key]}")
        for key in diff_a:
            print(f"  - {key}: {a[key]}")
        for key in diff_b:
            print(f"  + {key}: {b[key]}")
        print("}")
