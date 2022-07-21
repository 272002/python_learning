dct = {}

def max_frequency_of_a_word(letter):
    file = open('filewrite.txt','w')
    prs = letter.split()
    # print(prs)
    for j in range(len(prs)):
            if prs[j] in dct :
                dct[prs[j]] += 1
            else:
                dct.update({prs[j]:1})
        
            
    # file.write("Monday\n")
            # file.write(prs[j])
            # file.write(" ")
            file.write(prs[j])
            file.write(" ")
            file.write(str(dct.get(prs[j])))
            file.write("\n")
                
    file.close()
    return dct
    


file = open('wiki.txt','r')
data = file.read()
a = max_frequency_of_a_word(data)
print(a)
file.close()

# file = open('filewrite.txt','w')
# # file.write("Monday\n")
# file.writelines(a)
