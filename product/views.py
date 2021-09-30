from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from django.contrib.auth.models import User
from order.models import Wishlist
from accounts.models import Customer


def shop_details(request, id):
    query = Product.objects.get(id=id)
    print(query.category)
    related = Product.objects.filter(category=query.category).exclude(id=id)
    data = {
        'details': query,
        'related': related,
    }
    return render(request, "shop-details.html", data)


def all_goods(request):
    query = Product.objects.all()
    data = {
        'products': query,
    }
    return render(request, "shop-grid.html", data)


def like(request, id):
    try:
        user = User.objects.get(username=request.user.username)
        customer = Customer.objects.get(user=user)
        product = Product.objects.get(id=id)
        query = Wishlist.objects.create(customer=customer, product=product)
        query.save()
        messages.success(request, "Product has been added to wishlist.")
        return redirect("index")
    except Exception as e:
        messages.success(request, "Product has already exists in wishlist.")
        return redirect("index")


def wishlist(request):
    try:
        user = User.objects.get(username=request.user.username)
        customer = Customer.objects.get(user=user)
        query = Wishlist.objects.filter(customer=customer)
        return render(request, "order/wishlist.html", {'wishlist': query})
    except Exception as e:
        messages.error(request, "Wishlist error!")
        return render(request, "order/wishlist.html")


def cat_details(request, id):
    query = Product.objects.filter(category=id)
    data = {
        'products': query,
    }
    return render(request, "shop-grid.html", data)
