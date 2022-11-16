def insertionSort(myList):
    for i in range(1,len(myList)):
        temp = myList[i]
        j = i-1
        while temp < myList[j] and j>-1:
            myList[j+1] = myList[j]
            myList[j] = temp
            j = j-1           
    return myList
           