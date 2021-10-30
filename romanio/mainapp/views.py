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
            "category2": Category.objects.filter(id__gt=1),
            "categories": Category.objects.all(),
            "pr": Product.objects.get(pk=1)
        }

        return render(request, "index.html", context)


class CatalogPage(View):


    def get(self,request, *args, **kwargs,):
        context = {
            "categories": Category.objects.all(),
            "products": Product.objects.filter(category__slug=self.kwargs['slug_url']),
            "prod": Product.objects.filter(category__slug=self.kwargs['slug_url'])[0]

        } 
        return render(request, "category/shop-sidebar.html", context)


class ProductDetail(View):


    def get(self,request, *args, **kwargs,):
        
        context = {
            "product": Product.objects.filter(slug=self.kwargs['slug_product']),
            "products": Product.objects.filter(category__slug=self.kwargs['slug_url']),
        }
        return render(request, "category/product_page.html", context)


class ProductView(RedirectView):

    def get_redirect_url(self, *args, **kwargs) :

        product = get_object_or_404(Product, slug=self.kwargs['slug_product'])


        return reverse('product', kwargs = {'slug': product.slug})



def solo_product(request, slug_product):

    item = get_object_or_404(Product,slug=slug_product)

    context = {
    
        "item": item
    }


    return render(request, "category/product_page.html", context)






# class CategoryRedirectView(RedirectView):
#     permanent = True

#     def get_redirect_url(self, *args, **kwargs):
#         category = get_object_or_404(Category, name=self.kwargs['category'])
#         return reverse('category', kwargs={'slug': category.slug})





def contacts_page(request):
    return render(request, "navbar/contact/contact.html",)





