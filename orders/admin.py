from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['produkt']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'meno', 'priezvisko', 'email',
                    'adresa', 'PSC', 'mesto', 'zaplatene',
                    'created', 'updated']
    list_filter = ['zaplatene', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)