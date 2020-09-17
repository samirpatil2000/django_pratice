from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio', blank=True)

    def __str__(self):
        return self.title