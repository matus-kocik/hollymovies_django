from django.contrib import admin
from .models import Rating
from .forms import RatingForm

class RatingAdmin(admin.ModelAdmin):
    form = RatingForm

admin.site.register(Rating, RatingAdmin)
