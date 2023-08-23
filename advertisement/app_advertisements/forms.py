from django import forms
from .models import Advertisement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'for-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'for-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'for-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'for-check-input'}),
            'image': forms.FileInput(attrs={'class': 'for-control form-control-lg'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise forms.ValidationError('Заголовок не может начинаться с вопросительного знака!')
        return title

