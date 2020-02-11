from .scripts.utils import get_args
from .scripts.differ import get_diff_summary, print_diff

# from sourcer import source


def generate_diff():
    args = get_args()
    diff = get_diff_summary(args.first_file, args.second_file)
    print_diff(*diff)


if __name__ == "__main__":
    generate_diff()
