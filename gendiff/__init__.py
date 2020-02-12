from .scripts.differ import get_diff_summary, diff_to_str


def generate_diff(a, b, format="json"):
    diff_summary = get_diff_summary(a, b, format=format)
    return diff_to_str(*diff_summary)
