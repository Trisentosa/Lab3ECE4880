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


if __name__ == '__main__':
    app.run(debug=True)  # update flask server with changes we make
# team kiwi
