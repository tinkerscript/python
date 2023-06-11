from random import randrange

numerals = [str(randrange(10)) for _ in range(5)]

print(numerals)

with open('05.txt', 'w') as f:
    f.write(' '.join(numerals))

with open('05.txt') as f:
    print(sum([int(x) for x in f.read().split(' ')]))
