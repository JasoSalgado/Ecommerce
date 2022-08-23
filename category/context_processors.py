# category/context_processors.py
# Django modules

# My modules
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
    