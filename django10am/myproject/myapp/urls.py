from django.urls import path
from myapp import views
urlpatterns = [
    path('hello/',views.hello,name="hello"),
    path('sample_html/',views.sample_html,name="sample_html"),
    path('data/',views.data_all,name="data"),
    path('single_data/<pk>',views.single_data,name="single_data"),
    path('model_form/',views.register_modelform,name="register_modelform"),
    path('form/',views.register_form,name="register_form"),
    path('html_form/',views.html_form,name="html_form"),
    path('delete_user/<pk>',views.delete_user,name="delete_user"),
    path('cls_create/',views.Register_create.as_view(),name="cls_create"),
    path('cls_list/',views.Register_list.as_view(),name="cls_list"),
    path('cls_detail/<pk>/',views.Register_detail.as_view(),name="cls_detail"),
    path('cls_update/<pk>/',views.Register_update.as_view(),name="cls_update"),
    path('cls_delete/<pk>/',views.Register_delete.as_view(),name="cls_delete"),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name="logout"),
    path('custom_user/',views.custom_user_registration,name="custom_user"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
]

