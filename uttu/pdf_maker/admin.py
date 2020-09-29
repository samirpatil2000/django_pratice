from django.contrib import admin
from .models import postPdfTesting,PostWithMultipleImages,Images
# Register your models here.

admin.site.register(postPdfTesting)
admin.site.register(PostWithMultipleImages)
admin.site.register(Images)