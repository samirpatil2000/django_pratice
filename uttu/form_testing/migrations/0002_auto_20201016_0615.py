# Generated by Django 3.0.4 on 2020-10-16 06:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtesting',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 16, 6, 15, 11, 798934, tzinfo=utc)),
        ),
    ]