from unittest.mock import patch
import pytest
from simple_search import SimpleSearch

def test_init():
    simple_search = SimpleSearch()
    assert simple_search._search_base is None

def test__build_search_base():
    simple_search = SimpleSearch()
    simple_search._build_search_base("tests")

