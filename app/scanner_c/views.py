# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from flask_restx import Namespace, Resource, fields

scanner_n = Namespace('scanner', description='Cats related operations')


@scanner_n.route('/')
class Scanner(Resource):

    def get(self):
        """
        Returns list of white ip
        """
        result = {}


        return {'hello': 'hello world'}
        # return forbidden, 403



