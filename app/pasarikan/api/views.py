from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from ..models import Nelayan, Produk, Distrik, Kampung, OrderItem, Order
from .serializers import (
    NelayanSerializer, 
    ProdukSerializer, 
    DistrikSerializer, 
    KampungSerializer,
    OrderItemSerializer,
)

# Start API Nelayan GET, POST, UPDATE, DELETE, RETRIVE

class NelayanListView(ListAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer

class NelayanDetailView(RetrieveAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer

class NelayanCreateView(CreateAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer

class NelayanUpdateView(UpdateAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer

class NelayanDeleteView(DestroyAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer

# END API Nelanyan

# Start API Produk GET, POST,

class ProdukListView(ListAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ProdukDetailView(RetrieveAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ProdukCreateView(CreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

# END API Produk

# Start API Distrik GET, RETRIVE

class DistrikListView(ListAPIView):
    queryset = Distrik.objects.all()
    serializer_class = DistrikSerializer

class DistrikDetailView(RetrieveAPIView):
    queryset = Distrik.objects.all()
    serializer_class = DistrikSerializer

# END API Distrik

# Start API Kampung GET, RETRIVE
class KampungListView(ListAPIView):
    queryset = Kampung.objects.all()
    serializer_class = KampungSerializer

class KampungDetailView(RetrieveAPIView):
    queryset = Kampung.objects.all()
    serializer_class = KampungSerializer

# END API Kampung

# Start API Order

class OrderListView(ListAPIView):
    queryset = Order
    serializer_class = OrderItemSerializer