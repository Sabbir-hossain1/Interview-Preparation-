def recur_feb(n):
    if n<=1:
        return n
    else:
        return(recur_feb(n-1)+recur_feb(n-2))

nterms = 10
fblseries = []
for i in range(nterms):
    fblseries.append(recur_feb(i))
print(fblseries)
