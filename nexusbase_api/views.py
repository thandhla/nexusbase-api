from rest_framework import viewsets

from . import serializers
from .models import Card

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = serializers.CardSerializer
