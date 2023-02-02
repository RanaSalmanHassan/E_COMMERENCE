from django.shortcuts import render

from django.views.generic import ListView,DetailView

from .models import Product

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class home(ListView):
    model = Product
    template_name = 'shop/home.html'


class ProductDetails(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'shop/product_details.html'
