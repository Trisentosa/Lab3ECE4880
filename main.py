#Senior Design Lab 3

#1wasd
#jessie

# meesam 

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "asdjsdjkacjksdc" #encrypts cookies and session data related to website, it can be whatever we want

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tri")
def tri():
    return render_template("tri.html")

@app.route("/meesam")
def meesam():
    return render_template("meesam.html")

@app.route("/som")
def som():
    return render_template("som.html")

@app.route("/jessie")
def jessie():
    return render_template("jessie.html")
    

    



    


if __name__ == '__main__':
    app.run(debug=True)  # update flask server with changes we make



# team kiwi
