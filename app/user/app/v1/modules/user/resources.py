# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: resources.py
# @Date:   2018-08-18 17:00:27
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2018-11-22 10:37:48
from flask import request
from flask_restplus import Resource, Namespace

from app import db
from app.v1.model.user import User
from app.v1.extensions.auth import  role_required
from app.v1.extensions.auth.jwt_auth import  auth
from app.v1.utils.user_utils import get_all_users
from .serial import get_user_fields

user_ns = Namespace('user')

parser = user_ns.parser()
parser.add_argument('Authorization', type=str,
                    location='headers',
                    help='Bearer Access Token',
                    required=True
                    )


@user_ns.route('/')
class UserList(Resource):
    """
    列出所有用户
    过滤某个字段，在头部加上 X-Fields: email
    """
    @user_ns.doc('获取用户列表',parser=parser)
    @auth.login_required
    @role_required.permission(2)
    @user_ns.marshal_list_with(get_user_fields,envelope='data')
    def get(self):
        return get_all_users()


@user_ns.route('/<email>')
class DeleterUserRequired(Resource):
    # 删除用户，只有超级管理员才有权限，请求时携带角色为sa的access_token
    @user_ns.doc('删除用户',parser=parser,description='用户删除，需要超级管理员权限')
    @auth.login_required
    @role_required.permission(2)
    def delete(self, email):
        user = User.query.filter_by(email=email).first()
        # Get user if it is existed.
        if user is not None:
            # Delete action.
            db.session.delete(user)
            db.session.commit()

            print ("user {} deleted".format(user.username))
            return {"message": "user {} delete success.".format(user.username)}, 200
        else:
            return {"message": "user {} does not exist.".format(email)}, 404

    #@user_ns.expect(user_put_model,validate=True,location='body')
    #@user_ns.doc('更新用户信息')
    #def put(self):
    #    pass

@user_ns.route('/info')
class GetUserInfo(Resource):
    """
    列出所有用户
    过滤某个字段，在头部加上 X-Fields: email
    """
    # @user_ns.doc('获取用户列表',parser=parser)
    # @auth.login_required
    # @role_required.permission(2)
    # @user_ns.marshal_list_with(get_user_fields,envelope='data')
    @user_ns.param('token', required=True)
    def get(self):
        user_token = request.args.get('token')
        print (user_token)
        return {
                "roles": ['admin'],
                # "token": access_token,
                "introduction": '我是超级管理员',
                "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                "name": 'Super Admin'
            }