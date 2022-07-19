for i in range(3):
    password = input("Enter a password ")
    length = len(password)
    if i < 3:
   
        if len(password)<5 :
            i=i+1
            continue
        if not password.find('a-z'):
            i=i+1
            continue
        if not password.find('A-Z'):
            i=i+1
            continue
        if not password.find('0-9'):
            i=i+1
            continue
        if not password.find('@'or'#'or'$'or'%'):
            i=i+1
            continue
        else:
            print('correct password ')
            break





        

