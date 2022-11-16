import math
def primeInterval(x,y):
    primeList=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    break
            else:
                primeList.append(i)
    return primeList
print(primeInterval(2,7))