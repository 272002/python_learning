# ord() function tails the ASCII value of characters
# chr() fucntion return the Charter at given ASCII number.
# print(ord('a'))
# print(chr(97))

# s   =  'hello'
# w   =  ' bye'
# print( "concatenate ",(s+w))

from unicodedata import name


# full_name = '{fname} {lname}'.format(fname='Aman', lname = 'Jain') 
# print(full_name)

name=input("Enter name ")
sem = int(input("Enter semester "))
college = input("Enter college name ")

# full_name = '{name} is in {sem} semester of {college} college '.format(name = name , sem = sem ,college = college ) 
full_name = '{} is in {} semester of {} college '.format(name,sem,college) 

print( full_name )