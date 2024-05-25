from django.urls import path
from .views import AccountViewSet, DestinationViewSet

urlpatterns = [
    path('accounts/', AccountViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('accounts/<pk>/', AccountViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('destinations/', DestinationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('destinations/<pk>/', DestinationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
