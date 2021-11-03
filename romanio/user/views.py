from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import View

from .forms import UserRegForm




class UserSignIn(View):

    def get(self, request, *args, **kwargs):
        user_form = UserRegForm()
        return render(request, 'user/signin.html', {'form': user_form})

    def post(self, request, *args, **kwargs):
        user_form = UserRegForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
        print(UserRegForm(request.POST))   
        return HttpResponseRedirect('/')
        print(user_form.cleaned_data)
            

    def post(self, request, *args, **kwargs):   
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'user/signin.html', {'form':UserRegForm(request.POST)})
