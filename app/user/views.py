# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from flask_restx import Namespace, Resource, fields

user_n = Namespace('user', description='Cats related operations')


@user_n.route('/')
class User(Resource):

    def get(self):
        """
        Returns list of white ip
        """

        return {'hello': 'hello world'}
