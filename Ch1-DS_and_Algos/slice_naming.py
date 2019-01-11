"""
Problem:
    Your program has become a mess of hardcoded slice indices
    and you want to clean it up.
"""

# Solution: named slices.

record = '....................100 .......513.25 ..........'

# Run in interactive mode

"""
cost = int(record[20:32]) * float(record[40:48])

or,

SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])
"""
