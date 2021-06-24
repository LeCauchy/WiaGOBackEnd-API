from datetime import date
import re
from django.shortcuts import render
from .models import *
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NodeSerializer, NotifSerializer, StateSerializer

# Create your views here.

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node_R.objects.all()
    serializer_class = NodeSerializer


class NotifViewSet(viewsets.ModelViewSet):
    queryset = Notif.objects.all()
    serializer_class = NotifSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def create_node(request):
    serializer_context = {
        'request': request,
    }
    if(request.method == 'POST'):
        node = Node_R.objects.create(
            node_name = request.data['node_name'],
            ip_address = request.data['ip_address'],
            longitude = request.data['longitude'],
            latitude = request.data['latitude']
            )
        node_s = NodeSerializer(node, context=serializer_context)
        node.save()

        state = State.objects.create(
            ip_address = request.data['ip_address']
        )

        notif = Notif.objects.create(
            name = request.data['node_name'],
            ip_address = request.data['ip_address'],
            type = 'Creation'
        )

        notif_s = NotifSerializer(notif, context=serializer_context)
        state_s = StateSerializer(state, context=serializer_context)
        state.save()
        result = {
            "status": True,
            "data": notif_s.data
        }
        return Response(result, status=status.HTTP_200_OK)

