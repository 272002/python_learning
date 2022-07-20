lst = []
i = 0
while i > -1:
    p = input("Enter push , pop , stop and value ")
    
    prs = p.split()
    if (prs[0] == 'push'):
        
        lst.append(int(prs[1]))

    elif (prs[0] == 'pop'):
        
        lst.remove(int(prs[1]))

    elif (prs[0] == 'stop'):
        break
    
    i = i+1



print(lst)