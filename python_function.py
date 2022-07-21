# def greet():
#     print("hello world")
#     return  'hi'

# var = greet()
# print(var)

def factorial(n):
    fact  =1
    for i in range(1,n+1):
        fact = fact * i
    return fact
a = int(input("Enter number "))
fct = factorial(a)
print(fct)

def table(n):
    for i in range(1,11):
        print(n*i)

a = int(input("Enter number "))
table(a)

