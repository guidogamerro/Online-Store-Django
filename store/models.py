from datetime import datetime
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.forms import DateTimeField

class CategoryProd(models.Model):

    name = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "CateogryProd"
        verbose_name_plural = "CategoriesProd"

    def __str__(self):

        return self.name

class Product(models.Model):

    name = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryProd, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "store", null = True, blank = True)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Product"
        verbose_name_plural = "Products"