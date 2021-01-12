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

