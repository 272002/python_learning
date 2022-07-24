class add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add_(self):
        return f'{self.a + self.b}'

class multiply(add):
    def __init__(self, a, b):
        super().__init__(a, b)
    def add_(self):
            return f'{self.a*self.b}'


ad = multiply(3,4)
print(ad.add_())
