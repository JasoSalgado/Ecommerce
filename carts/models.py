# carts/models.py
# Django modules
from django.db import models

# My modules
from store.models import Product, Variation

class Cart(models.Model):
    """
    Cart model
    """
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    """
    Cart item model
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def subtotal(self):
        return self.product.price * self.quantity


    def __unicode__(self):
        return self.product