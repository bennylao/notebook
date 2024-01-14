from operator import itemgetter

p1 = ("Anna", 18, 70)
p2 = ("John", 20, 80)
p3 = ("Jony", 19, 95)
p4 = ("Json", 23, 120)

scores = (p1, p2, p3, p4)

list = sorted(scores, key=itemgetter(0, 1, 2))

print(list)