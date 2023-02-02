from django.db import models
from django.conf import settings

from shop.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_cart')
    items = models.ForeignKey(Product,on_delete=models.CASCADE) 
    item_quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return ('{} x {}'.format(self.item_quantity,self.items))

    def get_total(self):
         total = self.items.price * self.item_quantity
        #  float_total = format(total,'0.2f')
        #  return float_total
         return total    

class Order(models.Model):
    order_items = models.ManyToManyField(Cart) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)   
    ordered = models.BooleanField(default=False)    
    created = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=400,blank=True,null=True)
    order_id = models.CharField(max_length=400,blank=True,null=True)


    def get_totals(self):
        total = 0
        for order_item in self.order_items.all():
            total +=float(order_item.get_total())
            return total