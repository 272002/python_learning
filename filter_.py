def is_even(n):
    return n%2==0

a = filter(is_even,[1,2,3,4,12,13,1334])
a =list(a)
print(a)