from nose.tools import assert_equal
from ArraySequences import Anagram

class AnagramTest(object):
    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)

t = Anagram()
t.is_an_anagram(" og og go", "gggooo")
