from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/')
def index():
    return 'Main Page'


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'You used the POST method'
    elif request.method == 'GET':
        return 'You used the GET method'


if __name__ == '__main__':
    app.run()
