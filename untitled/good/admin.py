from django.contrib import admin
from good.models import *
# Register your models here.
#admin.site.register(Store)
admin.site.register(products)


@admin.register(Store)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['name']
