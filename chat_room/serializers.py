from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Room, Chat


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializers(serializers.ModelSerializer):
    creator = UserSerializers()
    invited = UserSerializers(many=True)

    class Meta:
        model = Room
        fields = ('creator', 'invited', 'creation_date', 'update_date')


class ChatSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Chat
        fields = ('user', 'text', 'date')


class ChatPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('room', 'text')
