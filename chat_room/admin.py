from django.contrib import admin

from .models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'invited_user',
        'creation_date',
        'update_date',
    )

    def invited_user(self, obj):
        return '\n'.join([user.username for user in obj.invited.all()])

    list_filter = ('creator',)

    class Meta:
        model = Room


class ChatAdmin(admin.ModelAdmin):
    list_display = (
        'room',
        'user',
        'text',
        'date',
    )
    list_filter = ('room',)

    class Meta:
        model = Chat


admin.site.register(Room, RoomAdmin)
admin.site.register(Chat, ChatAdmin)
