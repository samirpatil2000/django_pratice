# Generated by Django 3.0.4 on 2020-10-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_attri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=25000),
        ),
    ]