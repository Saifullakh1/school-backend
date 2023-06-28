# Generated by Django 4.2.2 on 2023-06-27 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_classes', to=settings.AUTH_USER_MODEL),
        ),
    ]