from django.db import models
from Product.models import *
from Stock.models import *
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import copy
# Create your models here.

contract_choices=[
    ('M','Mexanik'),
    ('A' ,'Avto'),
    ('H' ,"Hecne"),
]


class Sale(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    contract_type = models.CharField(max_length=1,choices=contract_choices, default='Hecne')
    contract_code = models.CharField(max_length=80)
    contract = models.CharField(max_length = 100, blank=True)
    reserved_status = models.BooleanField()
    reserved_date = models.DateField()
    sale_number = models.IntegerField()
    sold_time=models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.contract + ' ' + self.stock.product.product_article



class SalesLog(models.Model):
    sale=models.ForeignKey(Sale, null=True, default=None, on_delete=models.SET_NULL)
    updated_sale_number=models.IntegerField(blank=True, null=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sale.contract

        

# @receiver(post_save, sender=Sale)
# def saleslog_handler(sender, instance, *args, **kwargs):
#     sale= SalesLog(sale=instance.id, updated_sale_number = instance.sale_number)

#     sale.save()


@receiver(pre_save, sender=Sale)
def sale_handler(sender, instance, *args, **kwargs):
    instance.contract = instance.contract_type[0] + instance.contract_code
    check = 0

    try:
        num = Sale.objects.get(id = instance.id)
        prev_num = copy.copy(num.sale_number)
        if num:
            if instance.sale_number > prev_num:
                
                if instance.reserved_status == True:
                    check = instance.sale_number - prev_num
                    print(check)
                    instance.stock.reserved_number = instance.stock.reserved_number + check
                    
                    instance.stock.active_number = instance.stock.phsyical_number - instance.stock.reserved_number
                else:
                    instance.stock.phsyical_number = instance.stock.phsyical_number - instance.sale_number
                    instance.stock.active_number = instance.stock.phsyical_number -  instance.stock.reserved_number
            else:
                if instance.reserved_status == True:
                    check = prev_num - instance.sale_number
                    instance.stock.reserved_number = instance.stock.reserved_number - check
                    instance.stock.active_number = instance.stock.phsyical_number - instance.stock.reserved_number
                else:
                    instance.stock.phsyical_number = instance.stock.phsyical_number + check
                    instance.stock.active_number = instance.stock.phsyical_number -  instance.stock.reserved_number
    except:
        if instance.reserved_status == True:
            instance.stock.reserved_number = instance.sale_number
            instance.stock.active_number = instance.stock.phsyical_number - instance.stock.reserved_number

        else:
            instance.stock.phsyical_number = instance.stock.phsyical_number - instance.sale_number
            instance.stock.active_number = instance.stock.phsyical_number - instance.stock.reserved_number
            print(instance.stock.phsyical_number)
 
    instance.stock.save()

    
    

