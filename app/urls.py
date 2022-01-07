from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views

urlpatterns = [
    path('',views.index ,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='index'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood/',views.create_hood,name = 'create_hood'),
    path('hood/',views.hoods,name = 'hood'),
    path('hood/<str:neighbourHood_name>',views.single_hood,name='single_hood')
    
]