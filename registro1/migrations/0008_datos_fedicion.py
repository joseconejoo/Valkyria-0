# Generated by Django 2.1.3 on 2019-01-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro1', '0007_auto_20190121_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='fedicion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]