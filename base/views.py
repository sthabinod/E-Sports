from django.shortcuts import render
from product.models import Category, Product
import datetime
from .models import Information
from accounts.models import Customer
from django.contrib.auth.models import User
from order.models import Order, Wishlist


def index(request):
    three_days_a_head = datetime.datetime.now() - datetime.timedelta(days=3)

    information = Information.objects.get(id=1)
    categories = Category.objects.all()
    products = Product.objects.all()
    latest_product = Product.objects.all()

    expensive_product = Product.objects.filter(
        price__gte=50)[:3]

    cheapest_product = Product.objects.filter(
        price__lte=20)[:3]
    wishlist_count = 0
    try:
        user = User.objects.get(username=request.user)
        customer = Customer.objects.get(user=user)

        wishlist_count = Wishlist.objects.filter(
            customer=customer).count()
        print(wishlist_count)
    except Exception as e:
        print("NO LOVED")

    cart_item_count = 0
    try:
        user = User.objects.get(username=request.user)
        customer = Customer.objects.get(user=user)

        cart_item_count = Order.objects.filter(
            complete=False).count()
    except Exception as e:
        print("NO LOVED")

    data = {
        'categories': categories,
        'products': products,
        'latest_product': latest_product,
        'cheapest_product': cheapest_product,
        'expensive_product': expensive_product,
        'information': information,
        'wishlist_count': wishlist_count,
        'cart_item_count': cart_item_count
    }

    if request.method == "POST":
        print("POST REQUEST")
        search = request.POST.get("search")
        search_query = Product.objects.filter(name__contains=search)
        print(search_query)
        data['search'] = search_query
    else:
        print("No POST REQUEST..")

    return render(request, 'pages/index.html', data)


def contact(request):
    return render(request, 'contact.html')
