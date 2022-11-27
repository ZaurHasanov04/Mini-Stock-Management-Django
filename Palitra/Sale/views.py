from django.shortcuts import render, redirect
from .models import *
from Stock.models import *
from .forms import *
from django.http import HttpResponseRedirect, JsonResponse
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
        sale.save()
        return HttpResponseRedirect('saleslist')

    context={
        'adding':adding,
        'products':products
    }

    return render(request, 'addsales.html', context)


def to_update_sale(request,id):
    instance = Sale.objects.get(id=id)
    update_sale = SaleForm(instance=instance)
    if request.method == 'POST':
        sale = SaleForm(request.POST, instance=instance)
        sale.save()
        return HttpResponseRedirect('saleslist')

    return JsonResponse({'sale':update_sale})    
   


def to_delete_sale(request, id):
    print(id)
    sale=Sale.objects.get(id=id)
    print(sale)

    sale.delete()
    

    return redirect('saleslist')


    