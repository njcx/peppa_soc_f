# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com


from . import models
from . import serializers
from rest_framework_mongoengine import generics


class data1View(generics.ListCreateAPIView):
    queryset = models.data1.objects.all().order_by('siteid')
    serializer_class = serializers.data1Serializer


class data2View(generics.ListCreateAPIView):
    queryset = models.data2.objects.all().order_by('personid')
    serializer_class = serializers.data2Serializer
