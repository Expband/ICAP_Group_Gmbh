from flask_restful import Resource
from flask import request, render_template, make_response, redirect
from PresentationLayer.RegisterForm import Register
from BussinesLogicLayer.UserService import UserServise


class RegisterRequest(Resource):
    @staticmethod
    def get():
        form = Register()
        template = render_template('register.html', form=form)
        response = make_response(template)
        response.headers['Content-Type'] = 'text/html'
        return response

    @staticmethod
    def post():
        form = Register(request.form)
        userService = UserServise
        userService.store_data(form.data)
        userService.store_data_azure(form.data)
        return redirect('/login')
