from django.db.models import fields
from .models import *
from rest_framework import serializers

class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node_R
        fields = ['node_name',
                  'ip_address',
                  'longitude',
                  'latitude',
                  'date_creation']


        
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['ip_address',
                  'date_on']




class NotifSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notif
        fields = ['name',
                  'ip_address',
                  'type',
                  'date_on']


                  