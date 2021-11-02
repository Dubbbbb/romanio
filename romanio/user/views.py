from django.shortcuts import render
from django.views.generic.base import View



class UserSignIn(View):

    def get(self, request, *args, **kwargs):

        context = {

        }
        
        
        return render(request, "signin.html", context)