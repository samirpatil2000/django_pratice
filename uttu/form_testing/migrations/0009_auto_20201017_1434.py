# Generated by Django 3.0.4 on 2020-10-17 14:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_testing', '0008_auto_20201017_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formtesting',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 14, 33, 58, 792041, tzinfo=utc)),
        ),
    ]