from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.ProductListView.as_view(), name='ProductListView'),
    path('product/<pk>/', views.ProductDetailView.as_view(), name='ProductDetailView'),
    path('buymenu/<pk>/', views.BuyMenu, name='buymenu'),
]
