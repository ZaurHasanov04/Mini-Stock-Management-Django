from .views import *
from django.urls import path

urlpatterns=[
    path('', to_show_stock, name='stocklist'),
    path('stock/add', to_add_stock, name='addstock')
]