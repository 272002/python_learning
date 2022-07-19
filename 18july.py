# s = 'hello-world'
# print(s.split('-'))

# n = int(input('enter number '))
# for i in range(n):
#     operate = input("Enter operation you want to perform ")
#     lst = operate.split()

#     if lst[0] == 'add':
#         print('Addition is ' , int(lst[1])+int(lst[2]))

#     elif lst[0] == 'multiply':
#         print('multiplication is ' , int(lst[1])*int(lst[2]))
    
#     elif lst[0] == 'subtract':
#         print('subtraction is ' ,int(lst[1])-int(lst[2]))


n = int(input('enter number '))
for i in range(n):
    operate = input("Enter operation you want to perform ")
    lst = operate.split()
    l = len(lst)
    if lst[0] == 'add':
        sum = int(0)
        for i in range(1,l):
          
            sum =sum+int(lst[i])
        print('Addition is ' , sum)   

    if lst[0] == 'multiply':
        multiply = int(1)    
     
        for i in range(1,l):
            multiply  = multiply*int(lst[i])
        print('multiply is ' , multiply)







