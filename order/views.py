from django.shortcuts import render, get_object_or_404, redirect

from product.models import Product
from .models import Order
from accounts.models import Customer
from django.contrib.auth.models import User
from django.contrib import messages
import datetime


def cart_details(request):
    try:

        user = User.objects.get(username=request.user)
        cart_product = Order.objects.filter(complete=False, user=user)
        sum = 0
        total = []
        for cart in cart_product:
            sum = (cart.product.price*cart.quantity)+sum
            amt = cart.product.price*cart.quantity
            total.append(amt)
        data = {
            'cart': cart_product,
            'sum': sum,
            'total': total
        }

        return render(request, "order/shoping-cart.html", data)
    except Exception as e:
        return render(request, "order/shoping-cart.html")


def checkout(request):

    user = User.objects.get(username=request.user)
    cart_product = Order.objects.filter(
        complete=False, order_status=False, user=user)
    sum = 0
    total = []
    for cart in cart_product:
        sum = (cart.product.price*cart.quantity)+sum
        amt = cart.product.price*cart.quantity
        total.append(amt)
    data = {
        'cart': cart_product,
        'sum': sum
    }
    if request.method == "POST":
        date = datetime.date.today()
        street = request.POST.get('street')
        city = request.POST.get('city')
        postal_code = request.POST.get('zipcode')
        phone = request.POST.get('phone')
        complete = True
        cart_product = Order.objects.filter(
            complete=False, order_status=False, user=user)
        for cart in cart_product:
            Order.objects.filter(id=cart.id).update(
                order_date=date, street=street, city=city, postal_code=postal_code, phone=phone, complete=complete)
        messages.success(request, "Successfully ordered!")

        return redirect('my-order')
    return render(request, "order/checkout.html", data)


def my_order(request):
    try:
        user = User.objects.get(username=request.user)
        order_product = Order.objects.filter(
            complete=True, user=user)

        sum = 0
        for order in order_product:
            sum = order.product.price+sum
        data = {
            'order': order_product,
            'sum': sum,

        }

        return render(request, "order/tracking.html", data)
    except Exception as e:
        # No such order found
        return render(request, "order/my-order.html")


def add_to_cart(request, id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        user = User.objects.get(username=request.user.username)
        print(user)
        product = Product.objects.get(id=id)

        cart_product = Order.objects.filter(
            complete=False, order_status=False, user=user)
        obj_order_false = Order.objects.filter(product=product, complete=False)
        print("here")
        if Order.objects.filter(product=product).exists() and obj_order_false.exists():
            for cart in cart_product:
                cart_item_qty = cart.product.quantity-cart.quantity
            print(cart_item_qty)
            if cart.product.quantity >= 1 and cart_item_qty >= 0:
                Product.objects.filter(id=cart.product.id).update(
                    quantity=(cart.product.quantity-cart.quantity))
                messages.success(
                    request, "Product is successfully added to cart!")
                return redirect('cart-details')
            else:
                messages.success(
                    request, f'{cart.product.name} is out of stock.')
        else:
            Order.objects.create(product=product, user=user,
                                 quantity=quantity, complete=False)
            messages.success(
                    request, "Product is successfully added to cart!")
            return redirect('cart-details')


    else:
        print("NO POST METHODDDDDDDD")
    return redirect("index")


def payment(request):
    return render(request, "order/payment.html")


def delete_order_item(request, id):
    object_to_delete = Order.objects.get(id=id)
    object_to_delete.delete()
    messages.success(request, "Order deleted successfully!")
    return redirect("my-order")
