from django.contrib import admin

from .models import Category, Product, PizzaSize

admin.site.register((Category, Product, PizzaSize))
