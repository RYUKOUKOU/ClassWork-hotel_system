import flask
from system import read_info,save_info

def text(id):
    data= read_info(id)
    print(data)
text(1)