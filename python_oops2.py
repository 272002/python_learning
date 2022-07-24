class users:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def get_name(self):
        return f'The name is {self.name}'
    
    def get_contact(self):
        return f'The contact no. is {self.contact}'


class students(users):
    def __init__(self, name, contact,roll_no):
        super().__init__(name, contact)
        self.roll_no = roll_no

    def get_roll_no(self):
        return f'The roll no. is {self.roll_no}'

class Teacher(users):
    def __init__(self, name, contact,salary):
        super().__init__(name, contact)
        self.salary = salary

    def get_salary(self):
        return f'The salary is {self.salary}'

class bus(users):
    def __init__(self, name, contact,capacity):
        super().__init__(name, contact)
        self.capacity = capacity

    def get_capacity(self):
        return f'full details are is {self.name} {self.contact} {self.capacity}'



stu = students('Akshat','123456','12')
teachers = Teacher('Shivank','234567','560000')
conductor = bus('arpit', 456788,23)

# print(stu.get_name())
# print(stu.get_contact())
# print(stu.get_roll_no())

# print(teachers.get_name())
# print(teachers.get_contact())
# print(teachers.get_salary())

print(conductor.get_capacity())
