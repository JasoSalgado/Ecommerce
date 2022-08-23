# store/views.py
# Django modules
from django.shortcuts import render, get_object_or_404

# My modules
from .models import Product
from category.models import Category

def store(request, category_slug=None):
    # Filter by slug
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()

    else:
         # An istance loads all data from model product
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    } 
    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    """
    Page detail of product
    """
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }

    return render(request, "store/product_detail.html", context)