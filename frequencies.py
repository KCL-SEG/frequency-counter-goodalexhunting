"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import collections
def frequencies(items):
    counter = collections.Counter(items)
    return dict(counter)

