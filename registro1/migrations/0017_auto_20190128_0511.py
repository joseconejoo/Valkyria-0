# Generated by Django 2.1.3 on 2019-01-28 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registro1', '0016_auto_20190128_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='dingreso',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 1, 28, 9, 11, 15, 7673, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='datos',
            name='fedicion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 1, 28, 9, 11, 15, 7673, tzinfo=utc)),
        ),
    ]
