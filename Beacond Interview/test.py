with open('GFG.txt','r') as file:
    while True:
        c = file.read(1)
        if not c:
            break
        print(c)
    file.close()