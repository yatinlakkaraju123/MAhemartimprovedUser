from django.contrib import admin
from django.urls import path,include
from .views import home,index,detail,all_categories,profile,AddressView,remove_address,cart,remove_cart,plus_cart,minus_cart,checkout,category_products,add_to_cart,orders
app_name = 'store'
urlpatterns = [
    path('',home , name="home"),
     path('add-to-cart/', add_to_cart, name="add-to-cart"),
    path('accounts/',include("accounts.urls")),
    path('index/',index,name="index"),
     path('product/<slug:slug>/', detail, name="product-detail"),
    path('categories/',all_categories, name="all-categories"),
    path('accounts/profile/',profile,name="profile"),
    path('accounts/add-address/', AddressView.as_view(), name="add-address"),
    path('accounts/remove-address/<int:id>/', remove_address, name="remove-address"),
    path('cart/', cart, name="cart"),
    path('remove-cart/<int:cart_id>/', remove_cart, name="remove-cart"),
    path('plus-cart/<int:cart_id>/', plus_cart, name="plus-cart"),
    path('minus-cart/<int:cart_id>/', minus_cart, name="minus-cart"),
    path('checkout/', checkout, name="checkout"),
    path('<slug:slug>/', category_products, name="category-products"),
    path('orders/', orders, name="orders"),
  

]