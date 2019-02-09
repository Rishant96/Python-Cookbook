"""
Problem Statement:
    We want to eliminate the duplicate values in a sequence,
    but preserve the order of the remaining items.
"""

# Solution: If the values in the sequence are hashable,
#           the problem is easily solved using a set and a generator.


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
