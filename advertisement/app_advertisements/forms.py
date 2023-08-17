from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'for-control form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'for-control form-control-lg'})) # widget отвечает за то, как будет обрабатываться форма
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'for-control form-control-lg'}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'for-check-input'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'for-control form-control-lg'}))