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



"""For multilple images testing """

class PostWithMultipleImages(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)

    def __str__(self):
        return self.title


def get_image_filename(instance, filename):
    id = instance.post.id
    return "post_images/%s" % (id)

class Images(models.Model):
    post=models.ForeignKey(PostWithMultipleImages,on_delete=models.CASCADE,default=None)
    image=models.ImageField(upload_to=get_image_filename,verbose_name='Image')

    def __str__(self):
        return self.post.title
