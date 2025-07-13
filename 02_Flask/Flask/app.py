from flask import Flask
''''
it creates an instance of the flask class, which 
will be your WSGI (web server)
'''

## WSGI Apllication
app=Flask(__name__)

@app.route("/")
def welocme():
    return "Welcom to this Flask course. " \
    "Thise should be an amazing cource"

@app.route("/index")
def index():
    return "Welcome to the index page."

if __name__ == "__main__":
    app.run(debug=True)


