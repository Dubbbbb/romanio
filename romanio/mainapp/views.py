from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *


class HomePage(ListView):
    template_name = "index.html"
    model = Door



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update ({
            "door": Door.objects.all(),
            "window": Window.objects.all(),
        })
        return context



# def home_page(request):
#     return render(request, "index.html",)

def contacts_page(request):
    return render(request, "navbar/contact/contact.html",)
