from rest_framework import serializers
from apps.schools.models import School
from apps.classes.serializers import ClassForSchoolSerializer


class SchoolSerializer(serializers.ModelSerializer):
    classes = ClassForSchoolSerializer(read_only=True, many=True)

    class Meta:
        model = School
        fields = ('name', 'classes')

