# Generated by Django 3.0.4 on 2020-04-06 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uttu_1', '0019_author_book_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='headshot',
        ),
        migrations.RemoveField(
            model_name='author',
            name='salutation',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='city',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='country',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='state_province',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='website',
        ),
    ]
