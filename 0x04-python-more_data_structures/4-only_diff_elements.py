#!/usr/bin/python3

from typing import Set

def only_diff_elements(set_1: Set[str], set_2: Set[str]) -> Set[str]:
    """Returns a set containing elements present in only one of the two input sets."""
    return set_1.symmetric_difference(set_2)

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
print(sorted(list(only_diff_elements(set_1, set_2))))
