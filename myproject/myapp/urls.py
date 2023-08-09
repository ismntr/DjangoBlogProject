from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  
    path('kayit/', views.register, name='kayit'),
    path('giris/', views.login, name='giris'),
    path('cikis/', views.cikis, name='cikis'), 
    path('post/create/', views.post_create, name='post_create'), 
]
