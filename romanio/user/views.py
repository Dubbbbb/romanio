
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .forms import LoginForm, UserRegForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def logout_view(request):
    logout(request)
    return redirect('home')

class UserSignIn(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'user/signin.html', {'form':UserRegForm()})
        else:
            return redirect('home')


    def post(self, request, *args, **kwargs):   
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'user/signin.html', {'form':form})


class UserLogin(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'user/login.html', {'form':LoginForm()})
        else:
            return redirect('home')

    def post(self, requst, *args, **kwargs):
        form = LoginForm(requst.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                login(requst, user)
                return redirect('home')
            else:
                messages.error(requst, 'Ошибка входа. Проверьте вводимые данные.')
                return redirect('login')
        return render(requst, 'user/login.html', {'form':form})
            
