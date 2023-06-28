from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.students.models import Student
from apps.students import serializers
from apps.students.permissions import TeacherPermission
from django.core.mail import get_connection, EmailMultiAlternatives, EmailMessage
connection = get_connection()


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = (IsAuthenticated, TeacherPermission)


class StudentRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentSearchAPIView(generics.ListCreateAPIView):
    filterset_fields = ['full_name', 'email', 'student_class__name']
    search_fields = ['full_name', 'email', 'student_class__name']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = serializers.StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendMessageAPIView(APIView):

    def post(self, request):
        connection.open()
        text = request.data['text']
        class_name = request.data['class_name']
        students = Student.objects.filter(student_class__name=class_name).values_list('email', flat=True)
        reciever_list = list(students)
        email1 = EmailMessage(text, 'saifullakh35@gmail.com', reciever_list, connection=connection)
        email1.send()
        connection.close()
        return Response({"message": "send"}, status=status.HTTP_200_OK)
