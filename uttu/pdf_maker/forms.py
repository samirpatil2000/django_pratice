
from .models import PostWithMultipleImages,Images
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = PostWithMultipleImages
        fields = ('title', 'body', )


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', )

