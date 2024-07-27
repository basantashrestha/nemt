from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
# from .documents import *
# from .serializers import *
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     CompoundFilterBackend,
# )


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

# class PublisherDocumentView(DocumentViewSet):
#     document = NewsDocuemnt
#     serializer_class = NewsDocumentSerializer
#
#     filter_backends = [
#         FilteringFilterBackend,
#         CompoundFilterBackend
#     ]
#
#     search_fields = ('word' , 'wordTrans')
#     multi_match_search_fields = ('word' , 'wordTrans')
#     fields_fields = {
#         'word' : 'word',
#         'wordTrans' : 'wordTrans'
#     }

