from rest_framework import serializers

from .models import Collection, Card

class CardSerializer(serializers.ModelSerializer):
    collection = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ('title', 'data', 'collection')
