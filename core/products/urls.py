from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.ProductListView.as_view(), name='product-list'),
    path('car-list/', views.CarListView.as_view(), name='car-list'),
    path('news-list/', views.NewsListView.as_view(), name='news-list'),
]