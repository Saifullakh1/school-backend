from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from apps.teachers.models import Teacher


class TeacherRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'token']

    def get_token(self, user):
        tokens = AccessToken.for_user(user)
        token = str(tokens)
        return token

    def create(self, validated_data):
        return Teacher.objects.create_user(**validated_data)


class TeacherSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        tokens = AccessToken.for_user(user)
        token = str(tokens)
        return {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'token': token
        }