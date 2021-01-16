from unittest.mock import patch
import pytest
from simple_search import SimpleSearch

def test_init():
    simple_search = SimpleSearch()
    assert simple_search._search_base is None
