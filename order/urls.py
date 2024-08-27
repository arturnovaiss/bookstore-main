from django.urls import include, path
from rest_framework import routers
from order import viewsets

router = routers.SimpleRouter()
router.register('order', viewsets.OrderViewSets, basename='order')

urlpatterns = [
    path('', include(router.urls))
]
