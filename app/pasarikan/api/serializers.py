from rest_framework import serializers
from ..models import Nelayan

class NelayanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nelayan
        fields = (
            'id_nelayan',
            'nama',
            'distrik',
            'kampung',
            'ttl',
            'jekel'     
        )