# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from flask_restx import Namespace, Resource, fields

log_analysis_n = Namespace('log_analysis', description='Cats related operations')


@log_analysis_n.route('/')
class LogAnalysis(Resource):

    def get(self):
        """
        Returns list of white ip
        """

        return {'hello': 'hello world'}