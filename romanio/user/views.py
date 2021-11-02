from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from .forms import UserRegForm


class UserSignIn(View):

    def get(self, request, *args, **kwargs):

        
        return render(request, 'user/signin.html', {'form':UserRegForm()})

    def post(self, request, *args, **kwargs):   
        form = UserRegForm(request.POST)
        print(form.cleaned_data)
        return HttpResponseRedirect('/auth/')