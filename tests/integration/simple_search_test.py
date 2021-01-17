from unittest.mock import patch

from simple_search import SimpleSearch


@patch("builtins.input")
def test_simple_search(input_mock):
    input_mock.side_effect = ["def search", ":quit"]
    search = SimpleSearch()
    for result in search.start("tests"):
        assert (
            result
            == "tests/integration/simple_search_test.py: 100%\ntests/unit/search_test.py: 50%\n"
        )
