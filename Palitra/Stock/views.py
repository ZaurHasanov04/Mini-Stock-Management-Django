from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def to_show_stock(request):
    stock = Stock.objects.all()

    context = {
        'stock':stock
    }

    return render(request, 'stocklist.html', context)


def to_add_stock(request):

    stock = StockForm()

    if request.method == 'POST':
        stock = StockForm(request.POST)
        if stock.is_valid():
            stock.save()
            return redirect('stocklist')


    context={
        'stock':stock
    }

    return render(request, 'addstock.html', context)    