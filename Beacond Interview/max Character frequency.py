from collections import Counter
 
# initializing string
test_str = "GeeksforGeeks"
res = Counter(test_str)
print(max(dict(res).values())) # for maximu values 
print(max(res,key=res.get))  # for maximu values key
