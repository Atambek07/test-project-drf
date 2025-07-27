from django.shortcuts import render
from . import models, serializers
from rest_framework import generics

class ProductListView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class NewsListView(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewSerializer

class CarListView(generics.ListAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer