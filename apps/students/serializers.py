from rest_framework import serializers
from apps.students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class_name = serializers.ReadOnlyField(source='student_class.name', required=False)

    class Meta:
        model = Student
        fields = ('id', 'full_name', 'email', 'birthday', 'student_class', 'class_name', 'address', 'gender', 'image')

