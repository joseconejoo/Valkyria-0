# Generated by Django 2.1.3 on 2019-01-27 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro1', '0010_auto_20190127_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]