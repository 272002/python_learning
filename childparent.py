class grandparent:
    def __init__(self,name):
        self.name = name
        print(self.name)

        

class parent(grandparent):
    def __init__(self, name):
        super().__init__(name)
        print(self.name)
        

class child(parent):
    def __init__(self, name):
        super().__init__(name)


chl = child("Aman")
