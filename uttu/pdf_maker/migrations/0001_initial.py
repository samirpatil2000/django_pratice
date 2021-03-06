# Generated by Django 3.0.4 on 2020-09-17 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postPdfTesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=4000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog_image_1', models.ImageField(upload_to='media')),
            ],
        ),
    ]
