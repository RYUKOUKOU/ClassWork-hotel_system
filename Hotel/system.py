import json
import os
print("当前工作目录:", os.getcwd())

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)
def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("文件 'data.json' 未找到。请确保文件存在并且路径正确。")
        return None
    except Exception as e:
        print(f"加载数据时发生错误: {e}")
        return None

def save_info(fjh, zy, xm, dh, sj):
    try:
        room_id = int(fjh)
    except ValueError:
        print('无效的房间ID，请输入有效的整数。')
        return False

    data = load_data()
    if data:
        for room in data:
            if room.get('roomid') == room_id:
                room['state'] = zy
                room['name'] = xm
                room['phone'] = dh
                room['timestamp'] = sj
                save_data(data)
                return True
        print(f'在数据中找不到房间ID {room_id}。')
    else:
        print('未找到数据。')
    return False

def read_info(fjh):
    try:
        room_id = int(fjh)
    except ValueError:
        print('无效的房间ID，请输入有效的整数。')
        return False

    data = load_data()
    if data:
        for room in data:
            if room.get('roomid') == room_id:
                zy = room['state']
                xm = room['name']
                dh = room['phone']
                sj = room['timestamp']
                return zy, xm, dh, sj
        print(f'在数据中找不到房间ID {room_id}。')
    else:
        print('未找到数据。')
    return False

#print(save_info(103,True,'LHH1231','12345','123'))
#print(read_info(103))