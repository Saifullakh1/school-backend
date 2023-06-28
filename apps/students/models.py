from django.db import models
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from ..classes.models import Class

MALE = 'male'
FEMALE = 'female'


def send_message_to_email(email, class_name):
    send_mail(
        "Hello 👋🏻",
        f"Welcome to {class_name}",
        'saifullakh35@gmail.com',
        [email],
        fail_silently=False,
    )


class Student(models.Model):
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    birthday = models.DateField()
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='student_image', blank=True, null=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super(Student, self).save()
        if self.email:
            send_message_to_email(self.email, self.student_class.name)
