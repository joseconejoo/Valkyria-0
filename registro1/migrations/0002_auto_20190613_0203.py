# Generated by Django 2.2 on 2019-06-13 06:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('registro1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPrev',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñÑ]+$')])),
                ('apellido', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñÑ]+$')])),
                ('cedula', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='datos',
            name='apellido',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñÑ]+$')]),
        ),
        migrations.AlterField(
            model_name='datos',
            name='nombre',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Solo letras para el nombre por favor.', regex='^[a-zA-ZñÑ]+$')]),
        ),
    ]
