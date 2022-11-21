from django.urls import path
from .views import *


urlpatterns=[
    path('saleslist', to_show_saleslist, name='saleslist'),
    path('add', to_show_add_sales, name='show_adding_page'),
    path('saleslist/<id>/delete', to_delete_sale, name='delete_sale')
]