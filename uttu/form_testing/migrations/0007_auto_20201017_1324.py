# Generated by Django 3.0.4 on 2020-10-17 13:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_testing', '0006_auto_20201016_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtesting',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 13, 24, 27, 16751, tzinfo=utc)),
        ),
    ]
