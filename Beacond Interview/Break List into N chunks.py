# def divideChunks(l,n):
#     chlist = []
#     for i in range(0,len(l),n):
#         chlist.append(l[i:i+n])
#     return chlist

def divideChunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]
    

my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']
print(list(divideChunks(my_list,5)))