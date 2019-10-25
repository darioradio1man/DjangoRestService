from django.contrib import admin
from Message.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'playerFrom', 'playerTo', 'messageText',)


admin.site.register(Message, MessageAdmin)
