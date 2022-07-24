# class webseries:
#     def __init__(self,name,season,episode):
#         self.name = name
#         self.season = season
#         self.episode = episode
#         # print('I am hit ')
     
#     def myname(self):
#         return self.name
    
#     def episode_(self):
#         return f'{self.name} {self.episode} {self.season}'

# web_1 = webseries("Game of Thrones -",1,1)
# web_2 = webseries("Hatim",1,2)

# # print(web_1.name,web_2.name)

# # print(web_1.myname())
# print(web_2.episode_())


class Vechile:
    def __init__(self,brand,color):
        self.brand = brand 
        self.color = color

    def get_brand(self):
        return f'This brand is {self.brand}'


class car(Vechile):
    def __init__(self, brand, color,type_):
        super().__init__(brand, color)
        self.type_ = type_
        

    def get_color(self):
        return f'This brand is {self.color}'
    
    def get_type_(self):
        return f'This brand is {self.type_}'


sedan = car('toyota', 'suv','red')
print(sedan.get_brand())
print(sedan.get_color())
print(sedan.get_type_())

