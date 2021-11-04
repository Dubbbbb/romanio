from django import forms
from .models import CustomUser





class UserRegForm(forms.ModelForm):

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'coop_name')

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password2','Пароли не совпадают.')
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if email and CustomUser.objects.filter(email=email).exclude(username=username).exists():
            self.add_error('email', 'Указанный электронный адрес уже существует')
        phone_number = self.cleaned_data['phone_number']
        if phone_number and CustomUser.objects.filter(phone_number=phone_number).exclude(username=username).exists():
            self.add_error('phone_number', 'Этот мобильный номер уже существует')
        return super().clean()


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
