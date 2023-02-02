app_name = 'App_Order'
from django.urls import path
from . import views
urlpatterns = [
   path('add_to_cart/<pk>/',views.add_to_cart,name='add_to_cart')
]
