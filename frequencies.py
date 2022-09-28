"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from itertools import groupby
def frequencies(items):
    items = [str(x) for x in items]
    return {value: len(list(freq)) for value, freq in groupby(sorted(items))}
    


