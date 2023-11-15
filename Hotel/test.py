import json
from datetime import datetime

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

# 示例数据
person_data = {
    'roomid': '2',
    'is_active': True,
    'name': 'John Doe',
    'phone': '123-456-7890',
    'timestamp': str(datetime.now())
}

# 保存数据
save_data(person_data)

# 读取数据
loaded_data = load_data()

if loaded_data:
    print('Loaded Data:', loaded_data)
else:
    print('No data found.')
