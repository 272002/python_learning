dct = { 'fname' : 'gautam' , 'lname' : 'patni'}
# print(type(dct))
# print(dct['fname'])
# print(dct['company'])  # key error as no key is there

# print(dct.get('company' , 'not found'))  #if company key is not there

dct.update({'company':'regex'})
x = dct.pop('fname')
# print(x)
# print(dct)

dict_ = dct.copy()
print(dict_.items())
