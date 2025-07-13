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
    
if __name__ == "__main__":
    app.run(debug=True)

