from django.urls import path
from .views import product_create

urlpatterns = [
    path('create/', product_create, name='product_create'),
]
