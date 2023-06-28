from django.urls import path
from apps.schools import views

urlpatterns = [
    path('', views.SchoolAPIView.as_view(), name='schools')
]
