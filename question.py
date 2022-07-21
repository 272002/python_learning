dct = {}

def funt(fst):
    # print(fst)
    # print(len(fst))
    for i in range(len(fst)):
        prs = fst[i].split()
        # print(prs)
        for j in range(len(prs)-1):
            if prs[0] in dct :
                dct[prs[0]].add(prs[j+1])
            else:
                dct.update({prs[0]:set()})
                dct[prs[0]].add(prs[j+1])
    return dct
  

    


file = open('filename.txt','r')
data = file.readlines()
a = funt(data)
print(a)