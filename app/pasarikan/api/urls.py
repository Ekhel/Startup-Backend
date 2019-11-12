from django.urls import path, include

from .views import (
    NelayanListView, 
    NelayanDetailView,
    NelayanCreateView,
    NelayanUpdateView,
    NelayanDeleteView, 
    ProdukListView, 
    ProdukDetailView, 
    DistrikListView, 
    DistrikDetailView, 
    KampungListView, 
    KampungDetailView
)

urlpatterns = [
    path('nelayan/', NelayanListView.as_view()),
    path('nelayan/create', NelayanCreateView.as_view()),
    path('nelayan/<pk>/update/', NelayanUpdateView.as_view()),
    path('nelayan/<pk>/delete/', NelayanDeleteView.as_view()),
    path('nelayan/<pk>', NelayanDetailView.as_view()),
    path('produk/', ProdukListView.as_view()),
    path('produk/<pk>', ProdukDetailView.as_view()),
    path('distrik/', DistrikListView.as_view()),
    path('distrik/<pk>', DistrikDetailView.as_view()),
    path('kampung/', KampungListView.as_view()),
    path('kampung/<pk>', KampungDetailView.as_view()),
    
]
