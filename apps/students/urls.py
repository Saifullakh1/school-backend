from django.urls import path
from apps.students import views


urlpatterns = [
    path('', views.StudentListCreateAPIView.as_view(), name='students'),
    path('student/<int:pk>', views.StudentRetrieveAPIView.as_view(), name='student_retrieve'),
    path('student/search', views.StudentSearchAPIView.as_view(), name='student-search'),
    path('student/send/message', views.SendMessageAPIView.as_view(), name='send-message')
]
