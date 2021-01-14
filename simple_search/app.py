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
        self._search_base = {}
        for root, _, files in os.walk(path):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    with open(file_path, "r") as file_content:
                        for line in file_content:
                            for word in line.split():
                                self._search_base.setdefault(word, set()).add(
                                    file_path
                                )
                except UnicodeDecodeError as err:
                    logger.warning(
                        "UnicodeDecodeError: {0} not indexed. {1}".format(
                            file_path, err
                        ),
                    )

    def start(self, path: str) -> Generator[str, None, None]:
        """start simple search work function
        :param path: path to diectory containing text files
        :yield: string result which could be scores or not found,
            OR quit start function return None
        """
        if path is None:
            raise ValueError("No directory given to index.")

        self._build_search_base(path)
        while True:
            print("search>", end="")
            words = input()
            if words == ":quit":
                print("Bye.")
                break

            res = self.get_scores(words)
            result = ""
            if res:
                for filepath, score in res:
                    result += "{}: {:.0%}\n".format(filepath, score)
            else:
                result = "no matches found"
            yield result

    def get_scores(self, words: str) -> TypeCount:
        """get files scores
        :param words: words given on the prompt
        :return: a list of top 10 (maximum) matching filenames in rank order,
                giving the rank score against each match
        """
        word_set = set(words.split())
        num_words = len(word_set)
        scores = Counter()
        for word in word_set:
            for filepath in self._search_base.get(word, []):
                scores[filepath] += 1 / num_words

        return scores.most_common(10)
