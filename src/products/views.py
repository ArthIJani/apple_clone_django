from django.shortcuts import render
from products.models import NewProductCard, ProductCard

def store_view(request, *args, **kwargs): 
    my_title = "Store"
    html_template = "Store.html"
    cards = NewProductCard.objects.all()
    products = ProductCard.objects.all()
    my_context = {
        "page_title": my_title,
        'cards': cards,
        'products': products,
    }
    return render(request, html_template, my_context)

def mac_view(request, *args, **kwargs): 
    my_title = "Mac"
    html_template = "mac/mac.html"
    my_context = {
        "page_title": my_title,
    }
    return render(request, html_template, my_context)