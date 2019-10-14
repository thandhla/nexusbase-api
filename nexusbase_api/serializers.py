import json
from rest_framework import serializers
from .models import Collection, Card

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    attributes = serializers.JSONField()
    collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    """
    def validate(self, data):
        if self.instance:
            collection = instance.collection
        else:
            print('no instance')

            for attribute in json.loads(data['collection'].attributes):
                attribute = 

        #raise serializers.ValidationError("finish must occur after start")
        return data
    """

    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ['collection', 'created', 'updated']
