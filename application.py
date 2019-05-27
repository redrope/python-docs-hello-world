from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Future home of RedRope Technologies, LLC"
