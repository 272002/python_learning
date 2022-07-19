n = int(input('enter number '))
j = 0

dict1= {
    'str' : [],
    'int' : [],
    'float' : []
}

for i in range(n):
    datatype = input("Enter a datatype ")
    value = input("input a value ")
    if datatype == 'str':
        dict1['str'].append(value)

    elif datatype == 'int':
        dict1['int'].append(value)
    
    elif datatype == 'float':
        dict1['float'].append(value)
    else :
        while j<1:
            dict1.update({datatype : []})
            j=j+1
        dict1[datatype].append(value)
        
print(dict1)