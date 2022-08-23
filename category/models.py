# category/models.py
# Django modules
from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    Model category
    """
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    # To change name in admin
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        # Return the url from store/urls.py
        return reverse('products_by_category', args=[self.slug])


    def __str__(self):
        return self.category_name


