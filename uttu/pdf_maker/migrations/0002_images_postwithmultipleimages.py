# Generated by Django 3.0.4 on 2020-09-28 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pdf_maker.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pdf_maker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostWithMultipleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.CharField(max_length=400)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=pdf_maker.models.get_image_filename, verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pdf_maker.PostWithMultipleImages')),
            ],
        ),
    ]