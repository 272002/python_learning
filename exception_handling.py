# try:
#     print(5/0)
# except:
#     print('error occur')

try:
    print(5/'a')
except ZeroDivisionError:
    print("error")
except TypeError:
    print("You can't divide by string ")

except:
    print("Something went wrong ")