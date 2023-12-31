from flask_restful import Resource
from flask import request, render_template, make_response, redirect
from PresentationLayer.LoginForm import Login
from BussinesLogicLayer.UserService import UserServise


class LoginRequest(Resource):
    @staticmethod
    def get():
        form = Login()
        template = render_template('login.html', form=form)
        response = make_response(template)
        response.headers['Content-Type'] = 'text/html'
        return response

    @staticmethod
    def post():
        form = Login(request.form)
        userservice = UserServise
        if userservice.compare_passwords(form.data['password'], userservice.get_password_sqlite(form.data['login'])) and userservice.compare_passwords(form.data['password'], userservice.get_password_azure(form.data['login'])):
            return "pass is ok in sqlite and azure"
        if userservice.compare_passwords(form.data['password'], userservice.get_password_sqlite(form.data['login'])):
            return "pass is ok in sqlite"
        else:
            return "pass not ok not in sqlite nor azure"
