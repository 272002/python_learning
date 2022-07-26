# class student:
#     id_ = 1;
#     fname = "Regex"


# obj  = student()
# print(obj.fname,obj.id_)

# obj1  = student()
# print(obj1.fname,obj1.id_)

# constructor L =: function( memory allocate => object )
# dunder functions ? 

# class student1:
#     def __init__(self , fname , id_):  # constructor  we can use another variable instead of self like y   x is a local variable a   
#         # print("hello")
#         # id_ = 1;
#         self.fname = fname         
#         self.id_ = id_ 

#     def studentinfo(self):
#         print(self.fname,self.id_)



# obj  = student1("bi",13)
# # print(obj.fname,obj.id_)
# obj.studentinfo()

# obj1  = student1("arpit", 12)
# # print(obj1.fname,obj1.id_)
# obj1.studentinfo()


from logging import info


class driver:
    def __init__(self,id_ ,name ,email):
        self.name = name
        self.id = id_ 
        self.email= email

    def info(self):
            print(self.id,self.name,self.email)


class customer(driver):
    def __init__(self, id_, name, email,wallet):
         super().__init__(id_, name, email)
         self.wallet = wallet

    def value(self):
        print(self.wallet)
        return super().info()
        



c1 = customer(12,"aman","abc@gmail.com",1000)
c1.value()

