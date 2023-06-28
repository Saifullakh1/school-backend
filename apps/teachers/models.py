from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Teacher(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    teacher_class = models.OneToOneField('classes.Class', on_delete=models.CASCADE, related_name='class_teachers', blank=True, null=True)
    item_name = models.CharField(max_length=50)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.email}"


