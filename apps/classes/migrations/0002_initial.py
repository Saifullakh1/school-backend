# Generated by Django 4.2.2 on 2023-06-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='student',
            field=models.ManyToManyField(related_name='student_classes', to='students.student'),
        ),
    ]
