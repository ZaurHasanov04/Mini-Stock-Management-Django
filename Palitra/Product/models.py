
from django.db import models

# Create your models here.


class ProductBrand(models.Model):
    brand_name = models.CharField(max_length=50, blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.brand_name


class Product(models.Model):
    brand=models.ForeignKey(ProductBrand, on_delete = models.CASCADE)
    product_article=models.CharField(max_length=250, blank= False, null=False)
    product_model = models.CharField(max_length=200, blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.brand.brand_name + ' ' + self.product_article + ' ' + self.product_model


    
    