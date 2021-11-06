from django import forms
from django.shortcuts import  get_object_or_404, redirect, render
from django.views.generic import View
from user.forms import AddPhoneForm
from user.models import CustomUser

from .models import *





class HomePage(View):
     
    def get(self, request, *args, **kwargs):
        context = {
            "products": Product.objects.all()[:6],
            "category1": Category.objects.get(pk=2),
            "category2": Category.objects.exclude(pk=2)
       }
        return render(request, "index.html", context)



class CatalogPage(View):

    def get(self,request, *args, **kwargs,):
        context = {
            "categories": Category.objects.all(),
            "products": Product.objects.filter(category__slug=self.kwargs['slug_url']),
            "prod": Product.objects.filter(category__slug=self.kwargs['slug_url'])[0]
        }       
        return render(request, "catalog.html", context)



class ProductDetail(View):

    def get(self, request, *args, **kwargs):
        context = {
            "product": Product.objects.filter(slug=self.kwargs['slug_url'])[:1],
            "related_product": Product.objects.filter(category__slug=self.kwargs['slug_category']).exclude(slug=self.kwargs['slug_url']),     
        }       
        return render(request, "product-single.html", context)


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        context = {
            "user":CustomUser.objects.get(username=request.user.username)
        }
        return render(request, 'profile/profile.html', context)

class PhoneAddView(View):

    def get(self, request, *args, **kwargs):
        if request.user.phone_number:
            return redirect('home')
        form = AddPhoneForm()
        
        return render(request, 'profile/phone_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddPhoneForm(request.POST)
        print(form.data)
        if form.is_valid():
            user = get_object_or_404(CustomUser,username=request.user.username)
            user.phone_number = form.cleaned_data['phone_number']
            user.coop_name = form.cleaned_data['coop_name']
            user.save()
            return redirect('home')
        return render(request, 'profile/phone_add.html', {'form':form})
        



