from itertools import product
from django.contrib import admin
from .models import CategoryProd, Product

class CategoryProdAdmin(admin.ModelAdmin):

    readonly_fields = ("created", "updated")


class ProductAdmin(admin.ModelAdmin):

    readonly_fields = ("created", "updated")

admin.site.register(CategoryProd, CategoryProdAdmin)

admin.site.register(Product, ProductAdmin)