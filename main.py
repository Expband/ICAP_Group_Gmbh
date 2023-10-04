import jinja2
from flask import Flask, render_template
from flask_restful import Api
from jinja2 import Environment
from PresentationLayer.LoginForm import Login
from PresentationLayer.RegisterForm import Register


app = Flask(__name__)
api = Api(app)
app.jinja_env = Environment(loader=jinja2.FileSystemLoader("templates"))
app.secret_key = "privat"

auth_data = {"username": "max", "password": "max"}


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    user_login = form.data['login']
    password = form.data['password']
    print(f"username {user_login} password {password}")
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    name = form.data['name']
    surename = form.data['surename']
    user_login = form.data['login']
    password = form.data['password']
    print(f"name {name} surename {surename} username {user_login} password {password}")
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
