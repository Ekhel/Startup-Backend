from django.urls import path, include

from .views import NelayanListView, NelayanDetailView, ProdukListView, ProdukDetailView

urlpatterns = [
    path('nelayan/', NelayanListView.as_view()),
    path('nelayan/<pk>', NelayanDetailView.as_view()),
    path('produk/', ProdukListView.as_view()),
    path('produk/<pk>', ProdukDetailView.as_view()),
]
