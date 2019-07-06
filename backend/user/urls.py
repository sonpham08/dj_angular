from rest_framework import routers
from django.urls import include, path
from .api import UserViewSet, LoggingViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'loggings', LoggingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
