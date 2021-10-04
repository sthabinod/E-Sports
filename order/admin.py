from django.contrib import admin

from .models import Order, Wishlist


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',  'product', 'user', 'quantity', 'phone', 'order_status', 'complete',
                    )
    search_fields = ('phone', 'order_status', 'order_date')
    autocomplete_fields = ('product', 'user')
    list_per_page = 10


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass
