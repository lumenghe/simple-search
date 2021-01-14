""" create class to do simple search """
import argparse
import logging
import os
from collections import Counter
from typing import Counter as TypeCount
from typing import Generator


logger = logging.getLogger(__name__)


class SimpleSearch:
    """class of a command line text search engine."""
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self._search_base = None

    def _build_search_base(self, path: str) -> None:
        """build search base dictionary
            specified by db_file
        :param path: path to diectory containing text files
        :return: None
        """
