import argparse
from .scripts.utils import get_path
# from differ import diff
# from sourcer import source


def main():
    parser = argparse.ArgumentParser(
        description="Difference Generator app", add_help=True
    )
    parser.add_argument("first_file", type=str, help="path for first file")
    parser.add_argument("second_file", type=str, help="path for second file")
    parser.add_argument(
        "-f", "--format", type=bool, help="set format of output"
    )
    args = parser.parse_args()
    print(args)
    get_path(args.first_file)
    get_path(args.second_file)
