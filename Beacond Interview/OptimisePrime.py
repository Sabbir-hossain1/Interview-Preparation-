import math
def checkPrime(x=2,y=0):
    numberList = list(range(x,y+1))
    # for i in range(2,int(math.sqrt(y))+1):
    for i in range(2,int(y**0.5)+1):
        for j in range(i*i,y+1,i):
            if j in numberList:
                numberList.remove(j)
    return numberList
print(checkPrime(2,500))