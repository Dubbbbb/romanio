from django.db.models.query_utils import select_related_descend
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic import View


from .models import *



class HomePage(View):
     
    def get(self, request, *args, **kwargs):

        context = {
            "products": Product.objects.all(),
            "category1": Category.objects.get(pk=1),
            "category2": Category.objects.filter(id__gt=1)
        }

        return render(request, "index.html", context)


class CatalogPage(View):

    def get(self,request, *args, **kwargs,):

        

        context = {
            "categories": Category.objects.all(),
            "products": Product.objects.filter(category__slug=self.kwargs['slug_url']),
            "title_product": Product.objects.filter(category__slug=self.kwargs['slug_url'])[0],

        } 
        
        return render(request, "category/shop-sidebar.html", context)
    # def get_queryset(self):
    #     return SubCategory.objects.filter(slug=self.kwargs['slug_url'])


def contacts_page(request):
    return render(request, "navbar/contact/contact.html",)





