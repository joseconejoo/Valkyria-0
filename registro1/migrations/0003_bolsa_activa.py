# Generated by Django 2.2 on 2019-06-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro1', '0002_auto_20190613_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolsa',
            name='activa',
            field=models.BooleanField(default=True),
        ),
    ]
