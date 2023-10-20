from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!!'

@app.route('/home')
def home():
    return "This is a home page."