# Generated by Django 3.0.4 on 2020-10-16 06:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_testing', '0002_auto_20201016_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtesting',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 6, 22, 53, 290569, tzinfo=utc)),
        ),
    ]