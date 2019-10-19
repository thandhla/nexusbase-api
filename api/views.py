from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CollectionSerializer, CardSerializer
from .models import Collection, Card

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request):
        collection = request.query_params.get('collection')
        if collection:
            queryset = Card.objects.filter(collection=collection)
        else:
            queryset = Card.objects.all()
        
        serializer = CardSerializer(queryset, many=True)
        
        return Response(serializer.data)
