# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from flask_restx import Namespace, Resource, fields

waf_n = Namespace('waf', description='Cats related operations')


@waf_n.route('/')
class Waf(Resource):

    def get(self):
        """
        Returns list of white ip
        """

        return {'hello': 'hello world'}
