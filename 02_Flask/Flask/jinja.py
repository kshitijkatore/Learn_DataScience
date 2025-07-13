## Building dynamic Url
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return f"Username: {username}, Password: {password}"
    else:
        return render_template("login.html")
    
''''   
## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is " + str(score)
'''

## Jinja2 Template Engine
'''
{{}} expression to peint output in html

{%...%} conditional, for loop

{#...#} this is for comments
'''

@app.route('/success/<int:score>')
def success(score):
    res =""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    return render_template('result.html',results=res)

## {%...%} conditional, for loop
@app.route('/successres/<int:score>')
def successres(score):
    res =""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score, 'res':res}
    
    return render_template('result1.html',results=exp)

if __name__ == "__main__":
    app.run(debug=True)