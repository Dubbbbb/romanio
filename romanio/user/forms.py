from django import forms
from django.db import models
from django.db.models import fields
from .models import CustomUser
from django.core.exceptions import ValidationError



class UserRegForm(forms.ModelForm):

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'coop_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Вы ввели разные пароли')
        return cd['password2']



