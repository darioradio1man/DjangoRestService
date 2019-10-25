from django.contrib import admin
from Inventory.models import Item, ItemType


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemType', 'quality', 'owner',)


admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Item, ItemAdmin)
