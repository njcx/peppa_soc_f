from __future__ import unicode_literals
from mongoengine import *

# Create your models here.
connect('soc', host='127.0.0.1', port=27017)  # 连接数据库


class data1(Document):
    siteid = StringField(max_length=45)
    title = StringField(max_length=45)
    lng = StringField(max_length=45)
    lat = StringField(max_length=45)

    meta = {'collection': 'raw_data1'}  # 数据库中的集合

    def __unicode__(self):
        return self.name


class data2(Document):
    personid = StringField(primary_key=True)
    siteid = StringField(max_length=45)
    xb = StringField(max_length=45)
    customername = StringField(max_length=45)
    onlinetime = StringField(max_length=45)
    offlinetime = StringField(max_length=45)
    areaid = StringField(max_length=45)
    birthday = StringField(max_length=45)

    meta = {'collection': 'raw_data2'}  # 数据库中的集合

    def __unicode__(self):
        return self.name

