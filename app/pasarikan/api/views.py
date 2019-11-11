from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import Nelayan, Produk
from .serializers import NelayanSerializer, ProdukSerializer

class NelayanListView(ListAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer

class NelayanDetailView(RetrieveAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer

class ProdukListView(ListAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ProdukDetailView(RetrieveAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer