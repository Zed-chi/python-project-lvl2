import os
import argparse


def get_file_content(filepath):
    with open(filepath, "r") as f:
        return f.read()


def get_path(path):
    path = os.path.normpath(path)
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    return path


def get_args():
    parser = argparse.ArgumentParser(
        description="Difference Generator app", add_help=True
    )
    parser.add_argument("first_file", type=str, help="path for first file")
    parser.add_argument("second_file", type=str, help="path for second file")
    parser.add_argument(
        "-f", "--format", type=bool, help="set format of output"
    )
    return parser.parse_args()


def diff_to_str(diff):
    result = "{"
    for key in diff["common_keys"]:
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
