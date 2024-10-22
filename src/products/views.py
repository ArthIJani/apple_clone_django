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

def iphone_view(request, *args, **kwargs): 
    my_title = "iPhone"
    html_template = "iphone/iphone.html"
    my_context = {
        "page_title": my_title,
    }
    return render(request, html_template, my_context)

def ipad_view(request, *args, **kwargs): 
    my_title = "iPad"
    html_template = "ipad/ipad.html"
    my_context = {
        "page_title": my_title,
    }
    return render(request, html_template, my_context)

def accessories_view(request, *args, **kwargs): 
    my_title = "Accessories"
    html_template = "accessories/accessories.html"
    my_context = {
        "page_title": my_title,
    }
    return render(request, html_template, my_context)