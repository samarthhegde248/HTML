from django.urls import path

from . import views
urlpatterns = [
	path("hello_api/",views.hello_api,name="hello_api"),
]