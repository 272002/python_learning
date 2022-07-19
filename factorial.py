fact = int(input('enter number '))
fact = fact+1
ans  = int(1)
if(fact == 1):
    ans = 1
else:
    for i in range(1,fact):
        ans = ans*i

print(ans)