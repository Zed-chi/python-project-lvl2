from .scripts.differ import get_diff_summary, diff_to_str


def generate_diff(a, b):
    diff_summary = get_diff_summary(a, b)
    return diff_to_str(*diff_summary)
