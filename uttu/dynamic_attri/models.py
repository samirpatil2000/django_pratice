from django.db import models

# Create your models here.
import random

from django.db import models
from django.conf import settings
from django.shortcuts import render,reverse
from django.db.models.signals import pre_save


# Create your models here.
from django.utils.text import slugify

CATEGORY_CHOICES=(
    ('S', 'MAC'),
    ('SW', 'MAC PRO'),
    ('OW', 'IPHONE')
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

productName=['iPhone 5s','iPhone 6s','iPhone Se','MacBook Air','MacBook Pro',
             'Sumsung Galaxy J7','Sumsung Galaxy J5','Sumsung Galaxy J2','Sumsung Galaxy J1 ace','LG mobile',
             'Asus Rog','Asus L3T01','Blackberry T9','Hp envy','Hp envy T56']
def default_product_name():
    n=random.randrange(0,len(productName))
    return productName[n]

def default_cat():
    cat_list=['Mobile','Laptops','Tv','Headphone','Earphone','Watch']
    n=random.randrange(0,len(cat_list))
    return cat_list[n]

def default_brand():
    brand_list=['Apple','Samsung','Lenovo','Xiaomi','MotoRolla','Google Pixels','Boat','Beat','Asus','HP','Tagg']
    n=random.randrange(0,len(brand_list))
    return brand_list[n]

def default_sub_cat():
    sub_cat_list=['Android','iPhone','Windows','Windows 7','Windows 8','Window 10','Window 10 lean','CromeBook','Smart Watch']
    n=random.randrange(0,len(sub_cat_list))
    return sub_cat_list[n]


class Category(models.Model):
    name=models.CharField(max_length=100,default=default_cat,unique=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(max_length=100,unique=True,default=default_sub_cat)
    category=models.ManyToManyField(Category)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=100,default=default_brand,unique=True)
    def __str__(self):
        return self.name




# alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = 'azsxdcfvgbqwertyhnmjuiklop'

def encryption(plaintext,k):
    alpha_updated=alphabet[26-k:26]
    alpha_updated+=alphabet[0:26-k]
    newtext=''
    for i in plaintext:
        newindex=alphabet.index(i)
        newtext+=alpha_updated[newindex]
    return newtext

def random_string_gen():
    n=random.randint(0,len(alphabet))
    m=random.randint(0,len(alphabet))
    str1=alphabet[n:n+5]
    str2=alphabet[m:m+6]
    string1 = encryption(str1,5)
    string2 = encryption(str2,5)
    if m==n:
        return random_string_gen
    random_string=f'{string1}-{string2}'

    return random_string


class Item(models.Model):
    title=models.CharField(max_length=100,default=default_product_name)
    price=models.IntegerField(default=random.randrange(15000,50000,1000))
    discount_price=models.IntegerField(blank=True,null=True)


    slug=models.SlugField(blank=True,unique=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True,null=True)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,null=True)


    desc=models.TextField(default="THis is desc ",max_length=500)
    favourite=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     blank=True,null=True)
    random_string_gen_for_slug=models.CharField(default=random_string_gen,max_length=100)

    def __str__(self):
        return self.title




def pre_save_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(f'{instance.title}-{instance.random_string_gen_for_slug}')
pre_save.connect(pre_save_slug,sender=Item)




""" THIS IS FOR TESTING DROPDOWN LIST"""


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    birthdate = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.name