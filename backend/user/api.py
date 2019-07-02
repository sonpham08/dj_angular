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
from .serializers import UserSerializer, LoggingSerializer
from product.models import Coin
from .models import Logging
import time
import moment
import calendar
import datetime

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
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

    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser, ]
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    # search_fields = ('id', 'first_name', 'last_name', 'email', 'username',)


    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter(name='phone',
                    in_=openapi.IN_QUERY,
                    required=True,
                    schema=None,
                    type=openapi.TYPE_INTEGER,
                    format=None,
                    enum=None,
                    pattern=None,
                    items=None,
    ),
    openapi.Parameter(name='email',
                    in_=openapi.IN_QUERY,
                    description="test manual param", 
                    type=openapi.TYPE_INTEGER
    )
    ])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)