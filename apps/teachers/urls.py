from django.urls import path
from apps.teachers import views

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='user-register'),
    path('login', views.LoginAPIView.as_view(), name='user-login'),
]