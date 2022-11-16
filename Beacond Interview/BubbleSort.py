def BubbleSort(myList):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if mylist[j]>myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
    return myList