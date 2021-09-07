import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello root world!'

@app.route('/test')
def hello():
    return 'Hello test!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
