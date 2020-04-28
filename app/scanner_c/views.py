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
        # if verify_token():
        #     try:
        #         temp = []
        #         white_ip_list = WhiteIpList.query.order_by(-WhiteIpList.id).all()
        #         if not white_ip_list:
        #             return nothing, 404
        #         for white_ip in white_ip_list:
        #             temp_dict = {}
        #             temp_dict['id'] = white_ip.id
        #             temp_dict['ip'] = white_ip.white_ip
        #             temp_dict['create_time'] = str(white_ip.create_time)
        #             temp.append(temp_dict)
        #         result['status'] = 0
        #         result['msg'] = 'success'
        #         result['white_ip_list'] = temp
        #         info(self, 'GET')
        #         return result, 201
        #     except Exception as e:
        #         current_app.logger.error(e)
        #         return server_error, 500

        return {'hello': 'hello world'}
        # return forbidden, 403



