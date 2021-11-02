from django.db.models.query_utils import select_related_descend
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.views.generic import View
from django.shortcuts import get_object_or_404


from .models import *





class HomePage(View):
     

    def get(self, request, *args, **kwargs):

        context = {

            "products": Product.objects.all()[:6],
            "category1": Category.objects.get(pk=1),
            "category2": Category.objects.filter(id__gt=1)

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





