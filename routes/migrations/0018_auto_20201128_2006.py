# Generated by Django 3.1.2 on 2020-11-28 20:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('routes', '0017_route_save'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='save',
        ),
        migrations.AddField(
            model_name='route',
            name='save_route',
            field=models.ManyToManyField(blank=True, related_name='save_route', to=settings.AUTH_USER_MODEL),
        ),
    ]
