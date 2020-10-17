from django.contrib import admin
from .models import Item,Category,Brand,SubCategory,Person,Country,City

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(SubCategory)
admin.site.register(Person)
admin.site.register(Country)
admin.site.register(City)