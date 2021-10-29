from django.db.models.query_utils import select_related_descend
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView

from .models import *


class HomePage(ListView):
    template_name = "index.html"
    model = Door


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = []
        products.extend(Door.objects.all())
        products.extend(Window.objects.all())
        context.update ({
            "products": products,
            "categories": SubCategory.objects.all(),
            "category1": SubCategory.objects.get(pk=1),
            "category2": SubCategory.objects.filter(pk__gt=1)

        })
        return context


class CatalogPage(ListView):
    template_name = "category/shop-sidebar.html"
    model = SubCategory
    context_object_name = 'categories'


    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        
        # categ = get_object_or_404(SubCategory, slug=slug_id)
        
        return context
    def get_queryset(self):
        return SubCategory.objects.filter(slug=self.kwargs['slug_url'])

# def home_page(request):
#     return render(request, "index.html",)

def contacts_page(request):
    return render(request, "navbar/contact/contact.html",)
