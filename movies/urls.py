from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/',views.login,name='login.html'),
    path('signup/',views.signup,name='signup.html')
]