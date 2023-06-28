from rest_framework import generics
from apps.schools.models import School
from apps.schools import serializers


class SchoolAPIView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer
