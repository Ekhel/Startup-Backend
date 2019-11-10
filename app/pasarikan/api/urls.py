from django.urls import path, include

from .views import NelayanListView, NelayanDetailView

urlpatterns = [
    path('', NelayanListView.as_view()),
    path('<pk>', NelayanDetailView.as_view()),
]
