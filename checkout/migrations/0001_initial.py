# Generated by Django 3.1.2 on 2020-10-25 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0002_auto_20201020_1957'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.membership')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
            ],
        ),
    ]
