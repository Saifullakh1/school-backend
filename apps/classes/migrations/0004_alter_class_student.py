# Generated by Django 4.2.2 on 2023-06-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('classes', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, related_name='student_classes', to='students.student'),
        ),
    ]
