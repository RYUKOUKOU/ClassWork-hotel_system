from flask import Flask,render_template,request,url_for
from system import read_info,save_info

main = Flask(__name__)
@main.route('/')
def index():
    return render_template('index.html')

def text(id):
    data= read_info(id)
    print(data)
text(1)