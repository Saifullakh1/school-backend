from django.db import models
# from apps.teachers.models import Teacher


class Class(models.Model):
    name = models.CharField(max_length=150)
    teacher = models.OneToOneField('teachers.Teacher', on_delete=models.CASCADE, related_name='teacher_classes')
    student = models.ManyToManyField('students.Student', related_name='student_classes', blank=True)

    def __str__(self):
        return self.name
