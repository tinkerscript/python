from functools import reduce

print(reduce(lambda previous, current: previous * current if current % 2 == 0 else previous, range(100, 1001)))
