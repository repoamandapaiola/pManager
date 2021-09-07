from django.contrib import admin

from .models import Meeiro, Client, EntryType, Entry, SalesEntry


@admin.register(Meeiro)
class MeeiroAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'rg']
    ordering = ['name']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['meeiro_id', 'entry_date', 'entry_type', 'entry_value', 'description']
    ordering = ['entry_date']


@admin.register(EntryType)
class EntryTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    ordering = ['description']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SalesEntry)
class SalesEntryAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'entry_date', 'sales_price', 'buy_price', 'description',
                    'product']
    ordering = ['entry_date']
