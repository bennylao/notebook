import collections

words = ['London', 'Oslo', 'Paris', 'Rome', 'Paris', 'Geneva',
         'Paris','Milano', 'Geneva', 'Paris', 'Granada', 'Rome',
         'Rome', 'London', 'London', 'Geneva', 'Geneva', 'Oslo',
         'Rome', 'Oslo', 'Oslo', 'Rome', 'Oslo', 'Rome', 'Geneva',
         'Granada', 'Granada', 'London']

x = collections.Counter(words)

print(x)


