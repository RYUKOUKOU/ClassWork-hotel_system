import json

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)
def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None

def save_info(fjh,zy,xm,dh,sj):
    data = load_data()
    if data:
        for room in data:
            if room.get('roomid') == fjh:
                room['state'] = zy
                room['name'] = xm
                room['phone'] = dh
                room['timestamp'] = sj
                save_data(data)
                return True
    print(f'房间号无效，你应该检查输入数字')
    return False

def read_info(fjh):
    data = load_data()
    if data:
        for room in data:
            if room.get('roomid') == fjh:
                zy = room['state']
                xm = room['name']
                dh = room['phone']
                sj = room['timestamp']
                return zy , xm , dh ,sj
    return None