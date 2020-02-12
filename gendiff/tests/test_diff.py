from gendiff import generate_diff
from gendiff.scripts.utils import get_file_content
import pytest


@pytest.fixture
def result():
    return get_file_content("./gendiff/tests/fixtures/result.txt")


def test_json_diff(result):
    diff = generate_diff(
        "./gendiff/tests/fixtures/a.json", "./gendiff/tests/fixtures/b.json"
    )
    assert diff == result

def test_yml_diff(result):
    diff = generate_diff(
        "./gendiff/tests/fixtures/a.yml",
        "./gendiff/tests/fixtures/b.yml",
        format="yml"
    )
    assert diff==result
