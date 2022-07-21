def number(lst):
    for i in range(1,len(lst)):
        p = 0
        if(int(lst[i])%2!=0):
            p = 1
            break
        
    return p



file = open('number.txt','r')

data  = file.readlines()
a = number(data)
print(a)
file.close()