from django.db import models

# Create your models here.
from django.utils import timezone


class FormTesting(models.Model):
    title = models.CharField(max_length=255,default='This is a title')
    notes = models.TextField(default='This is the not ')
    description = models.TextField(default='thia is decs')
    price = models.IntegerField(default=0, blank=True, null=True)
    offer = models.IntegerField(default=0, blank=True, null=True)
    time_added=models.DateTimeField(default=timezone.now())
    time_update=models.DateTimeField()


    def __str__(self):
        return self.title