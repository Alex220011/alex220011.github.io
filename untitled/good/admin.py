from django.contrib import admin
from good.models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(Store)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'arrived', 'store']
