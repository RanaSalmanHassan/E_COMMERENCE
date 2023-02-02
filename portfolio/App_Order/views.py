from django.shortcuts import render, get_object_or_404, redirect

from .models import Cart, Order
from shop.models import Product

from django.contrib.auth.decorators import login_required

# Messages
from django.contrib import messages


# Create your views here.

@login_required
def add_to_cart(request, pk):
    items = get_object_or_404(Product, pk=pk)
    # Do not sweat, Every item has primary key and Product also have specific primary key for every item so we are conparing that both are equal
    order_item = Cart.objects.get_or_create(
        items=items, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(items=items).exists():
            order_item[0].item_quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated")
            return redirect("shop:home")

        else:
            order.order_items.add(order_item[0])
            messages.info(request, 'This Item is added to your cart')
            return redirect("shop:home")

    else:
        order = Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        messages.info(request, 'This Item is added to your cart')
        return redirect('shop:home')
