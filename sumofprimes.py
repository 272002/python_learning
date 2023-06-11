import math
def prm(n):
    for j in range(2,int(math.sqrt(n))+1):
        if n%j == 0:
            return False
    return True

i = 4
sum = 6

while i<=200000:
    if (prm(i) == True):
        sum = sum + i
    i = i+1
print(sum)