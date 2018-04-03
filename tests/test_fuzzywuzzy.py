from unittest import TestCase

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class testFuzzyMatching(TestCase):
    def eval_similarity(self):
        fuzz.ratio("ACME Factory", "ACME Factory Inc.")