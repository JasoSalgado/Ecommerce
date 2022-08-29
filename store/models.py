# store/models.py
# Django modules
from itertools import product
from django.db import models
from django.urls import reverse

# My modules
from category.models import Category

class Product(models.Model):
    """
    Product model
    """
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        # Return to store/urls.py
        return reverse("product_detail", args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    """
    Variation manager to filter by color and size
    """
    def colors(self):
        return super(VariationManager, self).filter(variation_category="color", is_active=True)


    def sizes(self):
        return super(VariationManager, self).filter(variation_category="size", is_active=True)


variation_category_choice = (
    ("color", "color"),
    ("size", "talla"),
    
)
class Variation(models.Model):
    """
    Variation model:
    Color and size
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    # Creates an instance of VariationManager to be read
    objects = VariationManager()

    def __str__(self):
        # Display variations inside cart items
        return self.variation_category + ':' + self.variation_value
