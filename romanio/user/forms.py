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
        fields = ('username', 'first_name', 'last_name', 'email', 'coop_name')

        # 'phone_number'

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password2','Пароли не совпадают.')
        return super().clean()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



