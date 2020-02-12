from gendiff import generate_diff
from gendiff.scripts.utils import get_file_content


def test_json_diff():
    result = get_file_content("./gendiff/tests/fixtures/result.txt")
    diff = generate_diff(
        "./gendiff/tests/fixtures/a.json", "./gendiff/tests/fixtures/b.json"
    )
    assert diff == result
