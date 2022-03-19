from django.urls import path
from .views import VRegristation

urlpatterns = [
    path('', VRegristation.as_view(), name='Authentication'),
]
