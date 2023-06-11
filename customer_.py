class customer:
    def __init__(self,id_,name,salary,year,email):
        self.name = name;
        self.id = id_;
        self.salary = salary;
        self.year = year;
        self.email = email;

    def printinfo(self):
        print(self.name,self.id,self.email,self.year,self.salary)

class employee(customer):
    def __init__(self, id_, name, salary, year, email,interestrate):
        super().__init__(id_, name, salary, year, email)
        self.interestrate = interestrate

    def info(self):
        super().printinfo()
        print("Salary per month ",(self.salary)/12)
        print("Interest received in a year ",(self.salary*self.interestrate*self.year))
        


emp1 = employee(123,"Arpit",12000,10,"abc@gmail.com",12)
emp1.info()

