position = 0

def move_player(by_amount):
    global position
    position += by_amount
    print(position)

for  x in range(0,10):
    move_player(x)