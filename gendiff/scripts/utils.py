import os
import argparse


def get_file_content(filepath):
    with open(filepath, "r") as f:
        return f.read()


def get_path(path):
    path = os.path.normpath(path)
    if os.path.isabs(path):
        print(path)
    else:
        path = os.path.join(os.getcwd(), path)
        print(path)


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
