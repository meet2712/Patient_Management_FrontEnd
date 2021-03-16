import flask
from flask import *
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test', )
def test(value):
    return render_template('test.html', value)


@app.route('/login', methods=['POST','GET'])
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
    # print(type(json_data))
    return render_template('test.html', value=json_data)


@app.route('/patient',  methods=['POST','GET'])
def patient():
    url = "https://patient-managment-api.herokuapp.com/patient"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(type(response.text))
    return render_template('trial.html')



@app.route('/signup', methods=['POST','GET'])
def signp():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
