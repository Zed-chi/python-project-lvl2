import argparse


def main():
    parser = argparse.ArgumentParser(description='Difference Generator app', add_help=True)
    parser.add_argument('first_file', type=str, help='path for first file')
    parser.add_argument('second_file', type=str, help='path for second file')
    parser.add_argument('-f', "--format", type=bool,)
    args = parser.parse_args()
    print(args)
