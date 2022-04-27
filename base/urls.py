from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.loginPage, name='loginpage'),
    path('logout/', views.logoutUser, name='logoutpage'),
    path('register/', views.registerPage, name='registerpage'),
    
    path('', views.home, name='home'),
    path('posts/<str:pk>', views.posts, name='posts'),

    path('create-post/' , views.createPost, name= "createpost"),
    path('update-post/<str:pk>' , views.updatePost, name= "updatepost"),
    path('delete-post/<str:pk>' , views.deletePost, name= "deletepost")
  
]
