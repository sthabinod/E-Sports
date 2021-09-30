from django.contrib import admin
from .models import Information


@admin.register(Information)
class AdminInformation(admin.ModelAdmin):
    pass


admin.site.site_header = "Easy mart"
admin.site.site_title = "Easy Mart"
admin.site.index_title = "Easy Mart Admin"
