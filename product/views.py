from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from django.contrib.auth.models import User
from order.models import Wishlist
from accounts.models import Customer
from base.models import Information


def shop_details(request, id):
    query = Product.objects.get(id=id)
    print(query.category)
    related = Product.objects.filter(category=query.category).exclude(id=id)
    data = {
        'details': query,
        'related': related,
    }
    return render(request, "pages/single-product.html", data)


def all_goods(request):
    information = Information.objects.all()
    categories = Category.objects.all()
    query = Product.objects.all()
    data = {
        'products': query,
        'categories':categories,
        'information': information,
    }
    return render(request, "pages/category.html", data)



def search(request):
    search_content = None
    information = Information.objects.all()
    if request.method == 'POST':
        search = request.POST.get("search")
        print(search)
        categories = Category.objects.all()
        search_content = Product.objects.filter(name__icontains=search)
    data = {
        'searches':search_content,
          'categories':categories,
         'information':information
    }
    return render(request, "pages/category.html",data)


def like(request, id):
    try:
        user = User.objects.get(username=request.user.username)
        product = Product.objects.get(id=id)
        query = Wishlist.objects.create(customer=user, product=product)
        query.save()
        messages.success(request, "Product has been added to wishlist.")
        return redirect("index")
    except Exception as e:
        messages.success(request, "Product has already exists in wishlist.")
        return redirect("index")


def wishlist(request):
    try:
        user = User.objects.get(username=request.user.username)

        query = Wishlist.objects.filter(customer=user)
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
