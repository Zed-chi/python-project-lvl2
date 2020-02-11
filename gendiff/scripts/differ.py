from json import loads
from .utils import get_file_content, get_path


def get_diff(filepath1, filepath2):
    a = loads(get_file_content("./a.json"))
    b = loads(get_file_content("./b.json"))
    diff_a = set(a.keys()).difference(set(b.keys()))
    diff_b = set(b.keys()).difference(set(a.keys()))
    common = set(a.keys()).intersection(set(b.keys()))
    return [a, b, diff_a, diff_b, common]


def print_json_diff(a, b, diff_a, diff_b, common):
    changed = []
    unchanged = []

    for k in common:
        if a[k] != b[k]:
            changed.append(k)
        else:
            unchanged.append(k)

    print("{")
    for k in unchanged:
        print(f"    {k}: {a[k]}")
    for k in changed:
        print(f"  - {k}: {a[k]}")
        print(f"  + {k}: {b[k]}")
    for k in diff_a:
        print(f"  - {k}: {a[k]}")
    for k in diff_b:
        print(f"  + {k}: {b[k]}")
    print("}")

    get_path("./asdas.re")
