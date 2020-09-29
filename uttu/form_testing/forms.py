from django.forms import ModelForm
from django import forms
from .models import FormTesting


class TestFrom(forms.ModelForm):
    class Meta:
        model=FormTesting
        #fields='__all__'
        fields=['title','notes','description','price','offer','time_update']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'notes': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.TextInput(attrs={'class': 'form-control', }),
            'time_update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            #  'offer': forms.IntegerField(attrs={'class': 'form-control', }),
            #  'price': forms.IntegerField(attrs={'class': 'form-control', }),

        }
        labels = {
            'title': ('title'),
            'notes': ('notes'),
            'description': ('description'),
            'time_update': ('time_update'),
            'offer': ('offer'),
            'price': ('price'),
        }
        error_messages = {

            'title': {
                'required': ('The field can not be empty')
            },
            'price': {
                'required': ('The field can not be empty')
            },
        }

