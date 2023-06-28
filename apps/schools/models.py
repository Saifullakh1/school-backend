from django.db import models
from apps.classes.models import Class


class School(models.Model):
    name = models.CharField(max_length=150)
    classes = models.ManyToManyField(Class, related_name='school_class', blank=True)

    def __str__(self):
        return self.name
