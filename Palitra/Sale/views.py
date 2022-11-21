from django.shortcuts import render, redirect
from .models import *
from Stock.models import *
from .forms import *
from django.http import HttpResponseRedirect
# Create your views here.


def to_show_saleslist(request):

    sales=Sale.objects.all()
    
    context={
        'sales':sales
    }

    return render(request, 'saleslist.html', context)


def to_show_add_sales(request):

    products = Stock.objects.all()
    adding=SaleForm()
    
    if request.method == 'POST':
        sale=SaleForm(request.POST)
        print(sale)
        print('hello')
        sale.save()
        return HttpResponseRedirect('saleslist')

    context={
        'adding':adding,
        'products':products
    }

    return render(request, 'addsales.html', context)


def to_delete_sale(request, id):
    
    sale=Sale.objects.get(id=id)

    sale.delete()
    

    return redirect('saleslist')


    