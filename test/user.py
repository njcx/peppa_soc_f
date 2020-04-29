# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 3:58 PM
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : rule_id.py


from test import get, post
from test import html_detail
from test import dict_to_json


header = {'content-type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36',
          }


user_detail = 'http://127.0.0.1:5000/user/detail'
user_login = 'http://127.0.0.1:5000/user/login'


class User(object):

    def __init__(self, host=None, https=False):

        self.user_detail_ = user_detail
        self.user_login_ = user_login

        if host:
            if https:
                self.user_detail_ = 'https://{host}/user/detail'.format(host=host)
                self.user_login_ = 'https://{host}/user/login'.format(host=host)
            else:
                self.user_login_ = 'http://{host}/user/login'.format(host=host)
                self.user_detail_ = 'http://{host}/user/detail'.format(host=host)

    def login(self):
        data = {'name':'njcx', 'password': 'njcx'}
        r = post(url=self.user_login_, data=dict_to_json(data))
        html_detail(r)

    def user_detail(self):

        header = {'content-type': 'application/json',
                  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36',
                  'X-token' :'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4ODE1MTU1NSwiZXhwIjoxNTg4MTU1MTU1fQ.eyJ1c2VyX25hbWUiOiJuamN4In0.vdgljMLqgESOdKycG1dL0ROfP912DJtSr0Bv-sY97yt8HBL-1h01JSgsrZyv4RJUBS6sVh1RpBoO-lzbYx_MKA'
                  }
        r = get(self.user_detail_, header=header)
        html_detail(r)


if __name__ == '__main__':

    user = User()
    user.login()
    user.user_detail()


