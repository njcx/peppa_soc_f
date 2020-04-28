# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from rest_framework_mongoengine import serializers
from . import models


class data1Serializer(serializers.DocumentSerializer):
    class Meta:
        model = models.data1
        fields = '__all__'


class data2Serializer(serializers.DocumentSerializer):
    class Meta:
        model = models.data2
        fields = '__all__'
