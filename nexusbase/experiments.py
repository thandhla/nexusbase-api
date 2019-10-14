from django.http import HttpResponse
from nexusbase_api.serializers import CardSerializer

def test_view(request):
    card = CardSerializer(data={
        'collection': 1,
        'attributes': '{"field_1":"John","field_2":"Doe","field_3":"Johndoe@email.com"}',
    })

    if card.is_valid():
        response = card
    else:
        response = card.errors

    #print(response)

    return HttpResponse(response)
