from django.urls import path
from . import views

urlpatterns = [
    path('cart-details', views.cart_details, name="cart-details"),
    path('checkout', views.checkout, name="checkout"),
    path('my-order', views.my_order, name="my-order"),
    path('add-to-cart/<int:id>', views.add_to_cart, name="cart"),
    path('payment', views.payment, name="payment"),
    path('delete', views.delete, name="delete"),

]
