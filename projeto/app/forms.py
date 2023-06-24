from django import forms
from django.contrib.auth.models import User
from .models import InfoPlus

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class InfoPlusEditForm(forms.ModelForm):
    picture = forms.ImageField(required=True)

    class Meta:
        model = InfoPlus
        fields = ['picture']
