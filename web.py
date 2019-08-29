from flask import flask
app=flask(_name_)
 
@app.route('/')
def index():
 reurn'hello, world'
