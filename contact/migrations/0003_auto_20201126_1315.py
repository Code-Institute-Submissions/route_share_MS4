# Generated by Django 3.1.2 on 2020-11-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20201126_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='post_date',
            new_name='contact_date',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='post_user',
            new_name='contact_user',
        ),
        migrations.AlterField(
            model_name='contact',
            name='copy_myself',
            field=models.BooleanField(blank=True),
        ),
    ]
