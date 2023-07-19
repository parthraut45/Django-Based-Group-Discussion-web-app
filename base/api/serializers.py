from rest_framework import routers, serializers, viewsets
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializers(ModelSerializer):
    class Meta:
        model = Room
        fields ='__all__'