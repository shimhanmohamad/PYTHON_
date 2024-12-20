class GameObject:
    def __init__(self,name,x_pos,y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    
game_object = GameObject("Shimhan",89,90)
print(game_object.name)