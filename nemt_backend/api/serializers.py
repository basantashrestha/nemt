from rest_framework import serializers

from .models import Item
from .documents import  *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #fields = ('word', 'wordTrans')
        fields = ('__all__')
