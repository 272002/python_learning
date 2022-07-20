dct = {}

while True:
    inp = input("Enter subject and name ")
    prs = inp.split()

    if (prs[0] == 'stop'):
        break
    else:
        if prs[0] in dct :
            dct[prs[0]].add(prs[1])
        else:
            dct.update({prs[0]:set()})
            dct[prs[0]].add(prs[1])


print(dct)


