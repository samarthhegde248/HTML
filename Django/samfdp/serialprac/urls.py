from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'music_library', views.music_libraryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('index/', views.IndexView.as_view(), name='index'),
    path('index/<pk>/', views.DetailsView.as_view(), name='details')
]