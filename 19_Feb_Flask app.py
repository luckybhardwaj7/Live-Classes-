# importing Flask if doing in local system install flask as "pip install flask"
from flask import Flask
from flask import request
# creating a app variable
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" #</h1> is for html representation

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World1</h1>" 

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World2</h1>" 

@app.route("/test")
def test():
    a=5+6
    return (f"This is my function to run app {a}")

@app.route("/test2")
def test2():
    # import request before making a request
    data = request.args.get("x")
    return (f"this is my data input from my url {data}")
    # to get this executed successfully just use "/test2?x=lucky"
    

if __name__=="__main__":
    app.run(host="0.0.0.0")
