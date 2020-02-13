from .scripts.parsers import get_differ
from .scripts.utils import diff_to_str


def generate_diff(a, b, format="json"):
    differ = get_differ(format)
    diff_summary = differ(a, b)
    return diff_to_str(diff_summary)
