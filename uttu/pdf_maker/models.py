from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class postPdfTesting(models.Model):

    title=models.CharField(max_length=50)
    # sub_title=models.CharField(default="This is the subtitle of the post ",max_length=150)
    content=models.TextField(max_length=4000)
    date_posted=models.DateTimeField(default=timezone.now)
    blog_image_1=models.ImageField(upload_to='media')
    # blog_image_2=models.ImageField(Blank=True,Null=True,upload_to='media')
    # blog_image_3=models.ImageField(default='default.jpg',upload_to='media')
    # author =models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title