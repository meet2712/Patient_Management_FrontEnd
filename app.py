from flask import *
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('login.html')


@app.route('/validate', methods=['POST'])
def validate():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        url = "https://patient-managment-api.herokuapp.com/token"

        payload = {'username': username,
                   'password': password}

        response = requests.request("POST", url, data=payload)
        json_data = json.loads(response.text)
        return jsonify(json_data)
    return redirect(url_for("home"))



@app.route('/signup', methods=['POST','GET'])
def signp():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
