# print("hello")
# x = 5
# y = 6
# print(x + y)

# from __future__ import division
# from numpy import subtract


# a = 12
# b = 343
# multiply = a * b
# add = a + b
# subtract = a - b
# division = a / b

# print(" The addition is ", add)
# print(" The subtraction is ", subtract)
# print(" The multipication is ", multiply)
# print(" The division is ", division)
# print(type(add))
# comp=4 + 8j
# print( type( comp ) )

# sentence= ' Taking a string in python '
# print(sentence[4])
# print( len(sentence) )
# print( sentence[ 0 : 4 ])
# print(sentence[1 : 4 : 2])
# print(sentence[::])
# print(sentence [::-1])        
# print(sentence[-1 : -7 : -1])

# var1=input("Enter string ")
# var2=var1[::-1]
# if var1==var2 :
#     print("yes it is palindrome")
# else:
#     print("not palindrome")

# val1=input("Enter first a number ")
# val2=input("Enter second number ")

# print(" The area of square is ", int(val1)*int(val1))
# print(" The perimeter of rectange is ", 2*(int(val1)+int(val2)))

# for x in range(10):
#     print(4*int(x))


i=int(input("select 1 for rectangle , 2 for right triangle , 3 for area of square , 4 for circle ,5 for quit  "))

if(i==1):
    x=int(input( " enter length of rectangle "))
    y=int(input(" enter breadth of rectangle "))
    print(" The perimeter of rectangle is ", 2*(x+y))

elif(i==2):
    x=input(" enter length of triangle ")
    y=input(" enter breadth of triangle ")
    print("The area of triangle is ", (int(x)*int(y))/2)

elif(i==3):
    x=input(" enter side of square ")
    print("The area of square is ", int(x)*int(x))

elif(i==4):
    x=input(" enter radius of circle ")
    print("The area of circle is ", 3.14*int(x)*int(x))

else:
    quit()