from django.urls import path, include
from .models import *
from .views import *

urlpatterns = [
    path('', to_show_productlist, name = 'productlist'),
    path('add/', to_add_product, name='addproduct')
]