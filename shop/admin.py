from django.contrib import admin
from .models import Shop, Products, Category
# Register your models here.


class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Products)
admin.site.register(Category)

