from django.urls import path
from . import views
from myapp.views import post_update  

urlpatterns = [
    path('', views.post_list, name='post_list'),  
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('post/create/', views.post_create, name='post_create'), 
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/update/', post_update, name='post_update'),
    
]