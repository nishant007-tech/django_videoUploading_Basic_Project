from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_playlist/', views.playlist, name='playlist'),
    path('watch_playlist/', views.see_playlist, name='see_playlist'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('remove_post/<int:id>/', views.remove_post, name='remove_post'),
    path('remove_playlist/<int:id>/', views.remove_playlist, name='remove_playlist'),
    path('change_password', views.c_password, name='c_password'),
    path('upload_demo/', views.upload_demo, name='upload_demo'),
     path('remove_demo/<int:id>/', views.remove_demo, name='remove_demo'),
]
