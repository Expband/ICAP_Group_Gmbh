import jinja2
from flask import Flask
from flask_restful import Api
from jinja2 import Environment
from PresentationLayer.RegisterController import RegisterRequest
from PresentationLayer.LoginController import LoginRequest


app = Flask(__name__)
api = Api(app)
app.jinja_env = Environment(loader=jinja2.FileSystemLoader("templates"))
app.secret_key = "privat"


@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response


api.add_resource(RegisterRequest, '/register')
api.add_resource(LoginRequest, '/login')


if __name__ == "__main__":
    app.run(debug=True)
