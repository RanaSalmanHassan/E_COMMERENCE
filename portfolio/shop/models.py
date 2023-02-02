from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'              # An extra "s" won`t` be added in admin field

            


class Product(models.Model):
    image = models.ImageField(upload_to='product_images')
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    prieview_text = models.CharField(max_length=200,verbose_name='Priview Text')
    details_text = models.CharField(max_length=500,verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name