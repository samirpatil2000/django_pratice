# Generated by Django 3.0.4 on 2020-10-17 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_testing', '0007_auto_20201017_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtesting',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 14, 2, 7, 221508, tzinfo=utc)),
        ),
    ]