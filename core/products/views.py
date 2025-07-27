from django.shortcuts import render

from . import serializers, models
from rest_framework import generics

class RegPopView(generics.ListAPIView):
  queryset = models.Register_Population.objects.all()
  serializer_class = serializers.RegPopSerializer
