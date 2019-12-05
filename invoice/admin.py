from django.contrib import admin

from .models import *


class InvoiceAdmin(admin.ModelAdmin):
    pass


class VendorAdmin(admin.ModelAdmin):
    pass


class BuyerAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Invoice, InvoiceAdmin)

admin.site.register(Vendor, VendorAdmin)

admin.site.register(Buyer, BuyerAdmin)

admin.site.register(Item, ItemAdmin)