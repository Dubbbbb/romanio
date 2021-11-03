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
            

def register(request):
    if request.method == 'POST':
        
        user_form = UserRegForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            print(user_form.cleaned_data)
            # Save the User object
            new_user.save()
            return render(request, 'index.html', {'new_user': new_user})
    else:
        user_form = UserRegForm()
    return render(request, 'user/signin.html', {'form': user_form})