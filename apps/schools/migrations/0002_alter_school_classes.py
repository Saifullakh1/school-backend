# Generated by Django 4.2.2 on 2023-06-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_alter_class_student'),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='classes',
            field=models.ManyToManyField(blank=True, related_name='school_class', to='classes.class'),
        ),
    ]
