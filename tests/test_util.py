import re

from trellome.util import chain_or
from trellome.util import regex_match_with_prop

def test_chain_or():
    assert chain_or(
            lambda: 1 == 0,
            lambda: 1 == 2,
            lambda: 1 == 1
            )

    assert not chain_or(
            lambda: 1 == 0,
            lambda: 1 == 2,
            lambda: 1 != 1
            )


def test_regex_match_with_prop():
    rgx = re.compile('.*ray.*', re.X | re.M | re.S)
    assert regex_match_with_prop("name", rgx, {"name": "my name is ray, lalalal."})()
    assert not regex_match_with_prop("name", rgx, {"name": "my name is none, lalalal."})()
