from rest_framework import serializers
from ..models import Nelayan, Produk

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