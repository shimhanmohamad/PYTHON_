position = 0

def move_player():
    global position
    position += 1
    print(position)

for  x in range(0,10):
    move_player()