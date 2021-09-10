from django.contrib import admin

from .models import Product, Category


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'date_added')
    search_fields = ('name', 'price')
    # autocomplete_fields = ('email',)
    # raw_id_fields = ('email',)
    list_per_page = 4


@admin.register(Category)
class AdminCat(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    # autocomplete_fields = ('email',)
    # raw_id_fields = ('email',)
    list_per_page = 4
