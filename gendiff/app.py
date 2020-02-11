from .scripts.utils import get_args
from .scripts.differ import get_diff, print_json_diff

# from sourcer import source


def main():
    args = get_args()
    json_diff = get_diff(args.first_file, args.second_file)
    print_json_diff(json_diff)


if __name__ == "__main__":
    main()
