# Generated by Django 3.1.2 on 2020-11-28 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0015_auto_20201127_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='save',
        ),
    ]