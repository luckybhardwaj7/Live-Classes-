from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home_page():
    return render_template('index.html')
# this is only to get the calculator index page

# making a calculator 

# entering the data from the form 
@app.route('/math', methods=['POST'])
def math_operation():
    if (request.method=="POST"):
        ops = request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if ops==('add'):
            r = num1+num2
            result=(f'The sum of {num1} and {num2} is {r}')
        
        if ops==('subtract'):
            r = num1-num2
            result=(f'The subtraction of {num1} and {num2} is {r}')

        if ops==('multiply'):
            r = num1*num2
            result=(f'The productof {num1} and {num2} is {r}')

        if ops==('divide'):
            r = num1/num2
            result=(f'The division of {num1} and {num2} is {r}')
        
        return render_template('results.html',result=result)



# entering the data from a tool by using a post method

@app.route('/postman_action', methods=['POST']) #postman is a tool used worldwide for APIs
def math_operation1():
    if (request.method=="POST"):
        ops = request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        if ops==('add'):
            r = num1+num2
            result=(f'The sum of {num1} and {num2} is {r}')
        
        if ops==('subtract'):
            r = num1-num2
            result=(f'The subtraction of {num1} and {num2} is {r}')

        if ops==('multiply'):
            r = num1*num2
            result=(f'The productof {num1} and {num2} is {r}')

        if ops==('divide'):
            r = num1/num2
            result=(f'The division of {num1} and {num2} is {r}')
        
        return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")
