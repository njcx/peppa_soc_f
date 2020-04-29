# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: resources.py
# @Date:   2018-08-19 00:08:26
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2018-11-22 11:00:10

from flask import request
from flask_restplus import Resource,Namespace
from app.v1.model.user import User
from .serial import register_model, login_model, \
    refresh_token_model,logout_model
from app.v1.utils.user_utils import  save_new_user
from app.v1.utils.auth_utils import  Auth
from app.v1.errors import CustomFlaskErr as notice



auth_ns = Namespace('auth')

parser = auth_ns.parser()
parser.add_argument('Authorization',
                    type=str,
                    required=True,
                    location='headers',
                    help='Bearer Access Token')


######  API
@auth_ns.route('/register')
class RegisterRequired(Resource):
    """注册接口"""
    @auth_ns.doc('用户注册')
    @auth_ns.expect(register_model, validate=True)
    def post(self):
        data = request.json
        return save_new_user(data=data)

@auth_ns.route('/login')
class LoginRequired(Resource):
    """登录接口"""
    @auth_ns.doc('用户登录')
    @auth_ns.expect(login_model, validate=True)
    def post(self):
        post_data = request.json
        print(post_data)
        return Auth.login_user(data=post_data)

@auth_ns.route('/logout')
class Logout(Resource):
    """登出接口"""
    @auth_ns.doc('用户登出',parser=parser,body=logout_model)
    # @auth.login_required
    def post(self):
        post_data = request.json
        return Auth.logout(data=post_data)

@auth_ns.route('/refresh_token')
class RefreshTokenRequired(Resource):
    """刷新Token"""
    @auth_ns.doc('刷新Token',parser=parser,body=refresh_token_model)
    def post(self):
        post_data = request.json
        return Auth.refresh_token(data=post_data)

@auth_ns.route('/confirm/<confirm_token>', endpoint="confirm")
class ConfirmRquired(Resource):
    """登录接口"""

    @auth_ns.doc('用户邮件确认')
    # @auth_ns.expect(login_model, validate=True)
    @auth_ns.param('email', required=True)
    def get(self, confirm_token):

        # Get Confirm email
        confirm_email = request.args.get('email')

        # Check confirm email
        #if  validate_email(confirm_email, check_mx=True, verify=True):

        #    return {"message": "email invalid input."}, 423
        # use staticmethod verify confirm toke
        if User.verify_confirm_token(confirm_token, confirm_email):

            raise notice(status_code=200, return_code=30002,action_status=True)

        else:

            raise notice(status_code=202,return_code=20009, action_status=False)


