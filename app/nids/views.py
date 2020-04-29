# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from flask_restx import Namespace, Resource, fields

nids_n = Namespace('nids', description='Cats related operations')


@nids_n.route('/')
class Nids(Resource):

    def get(self):
        """
        Returns list of white ip
        """

        return {'hello': 'hello world'}