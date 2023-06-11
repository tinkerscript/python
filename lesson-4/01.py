from sys import argv

hours, rate, bonus = argv[1:]

print(int(hours) * int(rate) + int(bonus))
