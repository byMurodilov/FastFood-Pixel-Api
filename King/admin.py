from django.contrib import admin
from .models import FastFoodType, Food, Review


admin.site.register(FastFoodType)
admin.site.register(Food)
admin.site.register(Review)