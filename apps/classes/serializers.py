from rest_framework import serializers
from apps.classes.models import Class
from apps.students.serializers import StudentSerializer


class ClassSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True)

    class Meta:
        model = Class
        fields = ('name', 'teacher', 'students')


class ClassForSchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ('name', 'teacher')