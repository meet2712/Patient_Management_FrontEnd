import flask
from flask import *
import requests

try:

    from flask import Flask

    from flask import redirect, url_for, request, render_template, send_file
    from io import BytesIO

    from flask_wtf.file import FileField
    from wtforms import SubmitField
    from flask_wtf import Form
    import sqlite3

    print("All Modules Loaded .... ")
except:
    print(" Some Module are missing ...... ")

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


@app.route('/', methods=["GET", "POST"])
def index():
    form = UploadForm()
    if request.method == "POST":

        if form.validate_on_submit():
            file_name = form.file.data
            database(name=file_name.filename, data=file_name.read())
            print("FILE : {}".format(file_name=filename))
            return render_template("index.html", form=form)

    return render_template("index.html", form=form)


class UploadForm(Form):
    file = FileField()
    submit = SubmitField("Submit")


#
# @app.route('/')
# def home():
#     return render_template('index.html')


@app.route('/test', methods=['GET'])
def test(value):
    return render_template('test.html', value)


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form.get("username")
    password = request.form.get("password")
    url = "https://patient-managment-api.herokuapp.com/token"

    payload = {'username': username,
               'password': password}

    response = requests.request("POST", url, data=payload)
    json_data = json.loads(response.text)
    print(type(json_data))
    return render_template('test.html', value=json_data)


@app.route('/patient', methods=['POST', 'GET'])
def patient():
    url = "https://patient-managment-api.herokuapp.com/patient"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(type(response.text))
    return render_template('trial.html')


@app.route('/signup', methods=['POST', 'GET'])
def signp():
    return render_template('signup.html')


@app.route('/validate_signup', methods=['POST','GET'])
def validate_signup():

    import http.client

    conn = http.client.HTTPSConnection("patient-managment-api.herokuapp.com")
    payload = ''
    headers = {
        'accept': 'application/json'
    }
    w = "username"
    x = "name"
    y = "email"
    z = "password"
    string = "/users?name=" + w + "&username=" + x + "&password=" + y + "&usertype=" + z
    conn.request("POST", string, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

if __name__ == '__main__':
    app.run(debug=True)
