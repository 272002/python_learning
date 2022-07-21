# from asyncore import write


# file = open('demo.txt','r')
# data = file.read()
# data  = file.readlines()
# file.close()
# print(data)

# write a file

# file = open('demo.txt','w')
# file.write("Monday\n")
# file.writelines(['kaise ho\n'])
# file.close()

file = open('demo.txt','a')
file.write('this is a demo file2 ')
file.close()