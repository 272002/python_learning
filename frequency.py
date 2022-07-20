# n  =input('enter string ')
# map_ = {}

# for i in n:
    
#     if i in map_:
#         map_[i] += 1
#     else:
#         map_[i] = 1

# print(map_)


n  =input('enter string ')
n  = n.lower()
map_ = {}

for i in n:
    
    if i in map_:
        map_[i] += 1
    else:
        map_[i] = 1

print(map_)






