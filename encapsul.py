class vechile:
    _year = 1000    # notation for protected modifier
    __price = 100001  # denote private variable

class tatamotors(vechile):
    car_name = "harrier"


v1 = vechile()
# print(dir(v1))
print(v1._vechile__price)  #name manualing of __price to _vechile__price
# print(v1.__price)
t1 = tatamotors()
print(t1._year,t1._vechile__price)