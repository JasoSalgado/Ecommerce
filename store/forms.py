# store/forms.py
# Django modules
from django import forms

# My modules
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    """
    Review form
    """
    model = ReviewRating
    fields = ["subject", "review", "rating"]