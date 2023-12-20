from flask import Flask,render_template,request,url_for
from system import read_info,save_info

main = Flask(__name__)
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/room1.html')
def room1():
    return render_template('room1.html')
@main.route('/room2.html')
def room2():
    return render_template('room2.html')


if __name__ == '__main__':
    main.run(host='0.0.0.0', port=8000)