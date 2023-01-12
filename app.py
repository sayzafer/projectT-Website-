from flask import Flask, render_template, session, redirect, request, url_for
import sqlite3
import requests

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


def create_app():
    app.Flask(__name__)
    app.config["SECRET_KEY"] = "FesC9cBSuxakv9yN0vBY"
    return app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login_index")
def login_index():
    return render_template("login_index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        response = requests.get("http://139.144.161.179:8080/login/zafer@gmail.com/1234")
        email = request.form.get('email')
        psw = request.form.get('password')
        # respose to json
        json = response.json()
        print(json)
        if email == json["user"]["Mail"] and psw == json["user"]["Password"]:
            session["user_name"] = json["user"]["Name"]
            session["user_email"] = json["user"]["Mail"]
            session["user_psw"] = json["user"]["Password"]
            return redirect(url_for('login_index'))
        else:
            return render_template("login.html", message="Invalid Email or Password")
    return render_template("login.html")


@app.route("/signUp", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        response = requests.get("http://139.144.161.179:8080/login/zafer@gmail.com/1234")
        nationalID = request.form.get("kimlikno")
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        surname = request.form.get("surname")
        phone = request.form.get("phone")
        address = request.form.get("adress")
        s = "http://139.144.161.179:8080/signup/"+name+"/"+surname+"/"+password+"/"+email+"/"+address+"/"+phone+"/"+nationalID
        print(s)
        session["user_name"] = name
        session["user_email"] = email
        p = requests.post(s)
        print(p.json())
        return redirect(url_for("login"))
    return render_template("signUp.html")


@app.route("/list_cargos", methods=["POST", "GET"])
def list_cargos():
    response = requests.get("http://localhost:80/cargoall/zafer@gmail.com/1234")
    json = response.json()
    print(json)
    type = []
    weight = []
    volume = []
    value = []
    nodeID = []
    destNodeID = []

    for i in range(len(json["Cargos"])):
        type.append(json["Cargos"][i]["Type"])
        weight.append(json["Cargos"][i]["Weight"])
        volume.append(json["Cargos"][i]["Volume"])
        value.append(json["Cargos"][i]["Value"])
        nodeID.append(json["Cargos"][i]["NodeID"])
        destNodeID.append(json["Cargos"][i]["destNodeID"])
    print(type)

    return render_template("list_cargos.html", type=type, weight=weight, volume=volume, value=value, nodeID=nodeID,
                           destNodeID=destNodeID)


@app.route("/profile", methods=["POST", "GET"])
def profile():
    response = requests.get("http://139.144.161.179:8080/login/zafer@gmail.com/1234")
    json = response.json()
    print(json)
    name = json["user"]["Name"]
    surname = json["user"]["LastName"]
    money = json["user"]["Balance"]
    star = json["user"]["Star"]
    fullName = name + surname
    data = {"name": fullName, "money": money, "star": star}

    return render_template("profile.html", data=data)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)
