from django.shortcuts import render
from products.models import NewProductCard, ProductCard

def home_view(request, *args, **kwargs): 
    my_title = "Home"
    html_template = "home.html"
    cards = NewProductCard.objects.all()
    products = ProductCard.objects.all()
    my_context = {
        "page_title": my_title,
        'cards': cards,
        'products': products,
    }
    return render(request, html_template, my_context)