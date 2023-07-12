from django.contrib import admin

from core import models


@admin.register(models.Customer)
class Customer(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)
    search_help_text = 'Поиску по логину покупателя'


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    search_help_text = 'Поиску по названию товара'


@admin.register(models.Deal)
class Deal(admin.ModelAdmin):
    list_display = (
        'customer',
        'item',
        'total',
        'quantity',
        'date',
    )
    search_fields = ('customer', 'item',)
    search_help_text = 'Поиску по логину покупателя или названию товара'
