from flask import Flask

app = Flask("meu app")

@app.route('/')
def hello():
    return "Hello World"

|