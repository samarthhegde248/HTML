from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$', views.index, name='index'),
	path('music/', views.musicStore, name='musicStore'),
	url(r'^music/(?P<music_id>[0-9]+)/$', views.edtItem, name='edtItem'),
	path('deleteItem/<music_id>', views.deleteItem, name= 'deleteItem'),
	path('saveItem/<music_id>', views.saveItem, name= 'saveItem'),
	path('libraryapiview/', views.LibraryApiView.as_view(), name = 'LibraryApiView'),
	path('libraryapiview/<pk>', views.LibraryApiView.as_view(), name = 'LibraryApiViewupde'),
]