# Generated by Django 2.1.3 on 2019-01-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro1', '0018_auto_20190128_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='cedula',
            field=models.IntegerField(default='20.000.000'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='email',
            field=models.EmailField(default='ejemplo@go.com', max_length=254),
        ),
    ]