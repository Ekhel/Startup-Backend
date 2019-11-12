from rest_framework import serializers
from ..models import Nelayan, Produk, Distrik, Kampung

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

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = (
            'id_produk',
            'nama_produk',
            'deskripsi',
            'stock',
            'ukuran',
            'kondisi',
            'min_order',
            'harga'     
        )

class DistrikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrik
        fields = (
            'id_distrik',
            'nama_distrik'
        )

class KampungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kampung
        fields = (
            'id_kampung',
            'distrik',
            'nama_kampung'
        )