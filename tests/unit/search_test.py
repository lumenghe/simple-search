from unittest.mock import patch
import pytest
from simple_search import SimpleSearch

def test_init():
    simple_search = SimpleSearch()
    assert simple_search._search_base is None

def test__build_search_base():
    simple_search = SimpleSearch()
    simple_search._build_search_base("tests")

def test_start_path_none():
    simple_search = SimpleSearch()
    with pytest.raises(ValueError):
        scores = simple_search.start(None)
        for _ in scores:
            assert True

@patch("builtins.input")
def test_start_path_not_none(input_mock):
    input_mock.side_effect = ["def search", "dogs", ":quit"]
    simple_search = SimpleSearch()
    scores = simple_search.start("tests")
    for ret in scores:
        assert ret in [
            "tests/integration/simple_search_test.py: 100%\ntests/unit/search_test.py: 50%\n",
            "no matches found",
        ]

