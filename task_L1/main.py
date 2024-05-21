import numpy as np
import random

com_boat=(2,2,2,3,3,5)
#初期化
def initialize(H,W):
    space_csee = np.zeros((H, W))
    space_attacked=np.zeros((H, W))
    for boat_size in com_boat:
        placed = False
        while not placed:
            x = random.randint(0, space_csee.shape[0] - 1)
            y = random.randint(0, space_csee.shape[1] - 1)
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal' and y + boat_size <= space_csee.shape[1]:
                if np.all(space_csee[x, y:y+boat_size] == 0):
                    space_csee[x, y:y+boat_size] = boat_size
                    placed = True
            elif direction == 'vertical' and x + boat_size <= space_csee.shape[0]:
                if np.all(space_csee[x:x+boat_size, y] == 0):
                    space_csee[x:x+boat_size, y] = boat_size
                    placed = True
    print(space_csee)

initialize(10,10)