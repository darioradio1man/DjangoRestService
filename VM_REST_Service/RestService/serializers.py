from Player.models import Player
from GameMap.models import Location
from rest_framework import serializers
from Inventory.models import Item, ItemType
from Message.models import Message


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url', 'name', 'email', 'playerclass', 'level', 'position')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'locationId', 'description', 'locationType')


class ItemTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemType
        fields = ('url', 'name')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url', 'itemType', 'quality', 'owner')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'playerFrom', 'playerTo', 'messageText')
