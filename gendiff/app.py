from .scripts.utils import get_args
from gendiff import generate_diff

# from sourcer import source


def main():
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
