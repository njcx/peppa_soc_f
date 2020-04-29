# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from flask_restx import Namespace, Resource, fields

honeypot_n = Namespace('honeypot', description='Cats related operations')


@honeypot_n.route('/')
class Honeypot(Resource):

    def get(self):
        """
        Returns list of white ip
        """

        return {'hello': 'hello world'}