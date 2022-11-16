from collections import Counter
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
restul = Counter(test_str.split())
print(max(dict(restul).values()))