# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from flask_restx import Namespace, Resource, fields
from flask import request, jsonify, current_app
from peppa_soc import User as user_list
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import functools
import hashlib

user_n = Namespace('user', description='Cats related operations')


def str_md5(parm):
    if isinstance(parm, str):
        parm = parm.encode("utf-8")
    m = hashlib.md5()
    m.update(parm)
    return m.hexdigest()


def create_token(user_name):
    s = Serializer(current_app.config["SECRET_KEY"], expires_in=3600)
    token = s.dumps({'user_name': user_name}).decode("ascii")
    return token


def verify_token(token):
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        data = s.loads(token)
    except Exception:
        return None

    name = data['user_name']
    for user_ in user_list:
        if user_.get('name') == name:
            return user_


def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            token = request.headers["X-token"]
        except Exception:
            return jsonify(code=4103, msg='缺少参数token')
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return jsonify(code=4101, msg="登录已过期")
        return view_func(*args, **kwargs)

    return verify_token


@user_n.route('/detail')
class User(Resource):
    decorators = [login_required]

    def get(self):

        token = request.headers["X-token"]
        user_dict = verify_token(token)

        for user_ in user_list:
            if user_.get('name') == user_dict.get('name'):
                return user_

        # return jsonify(code=0, msg="成功", data=data)


@user_n.route('/login')
class Login(Resource):

    def post(self):
        res_dir = request.get_json()
        if res_dir is None:
            return jsonify(code=4103, msg="未接收到参数")
        name = res_dir.get("name")
        password = res_dir.get("password")
        if not all([name, password]):
            return jsonify(code=4103, msg="请填写name或passwd")
        if {'name': name, 'passwd': str_md5(password)} not in user_list:
            return dict(code=4103, msg="not in user list ")
        token = create_token(name)
        return dict(code=0, msg="成功", data=token)



# if __name__ == '__main__':
#
#     print(create_md5('xxx', 'xxx'))




