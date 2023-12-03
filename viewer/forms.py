from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }
