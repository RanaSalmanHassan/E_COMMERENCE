app_name = 'shop'
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home.as_view(),name='home'),
   path('product_details/<pk>/',views.ProductDetails.as_view(),name='product_details'),
]