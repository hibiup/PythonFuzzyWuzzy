from unittest import TestCase

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class testSimilarity(TestCase):
    def test_simple_ratio(self):
        print("Ratio: " + str(fuzz.ratio("ACME Factory", "ACME Factory Inc.")))

    def test_partial_ratio(self):
        ratio = fuzz.partial_ratio("ACME Factory", "ACME Factory Inc.")
        print("Ratio: " + str(ratio))
        self.assertEquals(100, ratio)

class testTokenise(TestCase):
    def test_token_sort_ratio(self):
        # Low matching ratio
        ratio = fuzz.partial_ratio('Barack Obama', 'Barack H. Obama')
        print("Ratio: " + str(ratio))

        # Better matching
        ratio = fuzz.token_sort_ratio('Barack Obama', 'Barack H. Obama')
        print("Ratio: " + str(ratio))
        self.assertEquals(92, ratio)

        ratio = fuzz.token_set_ratio('Barack Obama', 'Barack H. Obama')
        print("Ratio: " + str(ratio))
        self.assertEquals(100, ratio)


class testExtractFromMaze(TestCase):
    def test_extract(self):
        query = 'Barack Obama'
        choices = ['Barack H Obama', 'Barack H. Obama', 'B. Obama']
        scores = process.extract(query, choices)
        print(scores)
        self.assertEqual('B. Obama', scores[2][0] )

        topScore = process.extractOne(query, choices)
        print(topScore)
        self.assertEqual('Barack H Obama', topScore[0] )
