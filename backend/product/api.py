from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .pagination import StandardResultsSetPagination
from rest_framework import authentication, permissions,generics
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
# from .filters import UserFilter

from drf_yasg.utils import no_body, swagger_auto_schema
from drf_yasg import openapi

from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators import action
# from knox.models import AuthToken
from .serializers import ProductSerializer
from .models import Product
from .filters import ProductFilter
import time
import moment
import calendar
import datetime

class ProductViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return the given user.

    list:
        Return a list of all users.

    create:
        Create a new user.

    destroy:
        Delete a user.

    update:
        Update a user.

    partial_update:
        Update a user.
    """

    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (ProductFilter,)

    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter(name='name',
                    in_=openapi.IN_QUERY,
                    required=True,
                    type=openapi.TYPE_INTEGER,
    )
    ])
    def list(self, request, *args, **kwargs):
        return super(ProductViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ProductViewSet, self).retrieve(request, *args, **kwargs)