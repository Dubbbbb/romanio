from django.shortcuts import render



from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mainapp.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect

# @require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    if request.method == 'GET': 
        return redirect('cart_detail')
    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))

# def cart_update(request, prodict_id, quant)
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=prodict_id)
#     cart['quantity']

def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': Cart(request),
        'cart_product_form':CartAddProductForm(request.POST)
    }
    return render(request, 'cart/cart_detail.html', context)