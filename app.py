from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form_login', methods=['POST','GET'])
def index():
    return render_template('login.html')

@app.route('/form_signup', methods=['POST','GET'])
def signp():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
