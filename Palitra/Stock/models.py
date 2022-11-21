from django.db import models
from Product.models import *
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# Create your models here.


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    phsyical_number = models.IntegerField()
    reserved_number = models.IntegerField()
    active_number = models.IntegerField()
    product_insertion_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.product_article


@receiver(pre_save, sender = Stock)
def to_handle_presave_stock(sender, instance, *args, **kwargs):
    instance.active_number = instance.phsyical_number - instance.reserved_number
    
    instance.save()