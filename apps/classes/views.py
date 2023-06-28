from rest_framework import generics
from apps.classes.models import Class
from apps.classes import serializers


class ClassAPIView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = serializers.ClassSerializer

