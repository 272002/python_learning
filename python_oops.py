class webseries:
    def __init__(self,name,season,episode):
        self.name = name
        self.season = season
        self.episode = episode
        print('I am hit ')

web_1 = webseries("Game of Thrones -",1,1)
web_2 = webseries("Hatim",1,2)

print(web_1.name,web_2.name)