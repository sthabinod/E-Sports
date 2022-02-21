from django.contrib import admin
from .models import Information


@admin.register(Information)
class AdminInformation(admin.ModelAdmin):
    pass


admin.site.site_header = "E-sports Shop"
admin.site.site_title = "E-Sports Shop"
admin.site.index_title = "E-Sports Shop"
