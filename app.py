## flask app for hello world

from flask import flask
import pandas as pd

app=Flask(__name__)
@app.route('/')
def hello_world():
    return "hello world!"

if __name __== '__main__':
    app.run(host="0.0.0.0"),(post=5000)

