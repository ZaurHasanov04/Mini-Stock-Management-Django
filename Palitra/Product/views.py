from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.

def to_show_productlist(request):
    product = Product.objects.all()

    context = {
        'product':product
    }

    return render(request, 'productlist.html', context)


def to_add_product(request):
    product = ProductForm()

    if request.method == 'POST':
        product=ProductForm(request.POST)

        if product.is_valid():
            product.save()

            return redirect('productlist')

    context={
        'product': product
    }

    return render(request, 'addproduct.html', context)    
