from unicodedata import name
from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add/<int:product_id>/", views.add_product, name="Add"),
    path("remove/<int:product_id>/", views.remove_product, name="Remove"),
    path("subtract/<int:product_id>/", views.subtract_product, name="Subtract"),
    path("clean/", views.clean_cart, name="Clean"),
]