from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import Nelayan
from .serializers import NelayanSerializer

class NelayanListView(ListAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer

class NelayanDetailView(RetrieveAPIView):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer