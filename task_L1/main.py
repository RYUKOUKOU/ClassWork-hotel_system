import numpy as np
import random
import os

H,W=5,7
com_boat=(2,2,2,3,3)
bullet=10
cheat_mode=True
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
    return space_csee,space_attacked

def attack(x, y, space_csee, space_attacked):
    global bullet
    if bullet > 0:
        if 0 <= x < space_csee.shape[0] and 0 <= y < space_csee.shape[1]:
            bullet -= 1
            if space_csee[y,x] != 0:
                space_attacked[y,x] = 1
                print("打つ！")
                return True
            else:
                space_attacked[y,x] = 2
                print("ミス！")
                return False
        else:
            print("座標が範囲外です。")
            return False
    else:
        print("弾は残っていない。")
        return False

def cheat(space_csee):
    global cheat_mode
    if cheat_mode:
        print(space_csee)

    
def refresh_screen(space1, space2): 
    os.system('cls' if os.name == 'nt' else 'clear')
    cheat(space1)
    H, W = space2.shape
    print("攻撃結果:")
    print(" |" + "  ".join(str(i) for i in range(W)))
    print("".join("———" for i in range(W)))
    for i in range(H):
        row = [str(int(space2[i, j])) if space2[i, j] != 0 else "." for j in range(W)]#断点
        print(f"{i} " + "  ".join(row))

def main():
    space_csee, space_attacked = initialize(H,W)
    while bullet > 0:
        try:
            x = int(input("攻撃用の x 座標を入力してください: "))
            y = int(input("攻撃用の y 座標を入力してください: "))
            attack(x, y, space_csee, space_attacked)
            print(f"残り弾数: {bullet}")
        except ValueError:
            print("無効入力。 整数の座標を入力してください。")
        refresh_screen(space_csee,space_attacked)

if __name__ == "__main__":
    main()