
from stackoverflow.models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
          'comment': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }