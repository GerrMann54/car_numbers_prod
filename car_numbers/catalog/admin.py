from django.contrib import admin
from .models import *
# Register your models here.
class PlateAdmin(admin.ModelAdmin):
    list_display = ['number', 'region', 'car', 'owner']
    list_filter = ['region']

class RegionAdmin(admin.ModelAdmin):
    list_display = ['number', 'name']

admin.site.register(Plate, PlateAdmin)
admin.site.register(Region, RegionAdmin)
