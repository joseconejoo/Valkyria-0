# Generated by Django 2.1.3 on 2019-01-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro1', '0009_auto_20190125_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='apellido',
            field=models.CharField(default='ingrese apellido', max_length=200),
        ),
        migrations.AlterField(
            model_name='datos',
            name='nombre',
            field=models.CharField(default='ingrese nombre', max_length=200),
        ),
    ]