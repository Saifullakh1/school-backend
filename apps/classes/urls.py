from django.urls import path
from apps.classes import views

urlpatterns = [
    path('', views.ClassAPIView.as_view(), name='classes')
]