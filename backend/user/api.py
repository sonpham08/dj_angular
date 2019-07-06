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
from rest_framework.decorators import action
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
    openapi.Parameter(name='user-type',
                    in_=openapi.IN_QUERY,
                    required=True,
                    type=openapi.TYPE_INTEGER,
                    description="Fetch user by user_type\n"+
                        "Fetch all user by: -1\n"+
                        "Fetch staff by: 0\n"+
                        "Fetch customer by: 1"
                    ,
                    enum=[-1, 0, 1],
                    pattern=None,
                    items=None,
    ),
    ])
    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        user_type = int(request.GET.get('user-type', ''))
        if user_type == 1:
            queryset = queryset.filter(is_user=True)
        if user_type == 0:
            queryset = queryset.filter(is_staff_gun=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def me(self, request):
        req_user = request.user
        try:
            res = {
                "username": req_user.username,
                "id": req_user.id,
                "is_staff_gun": req_user.is_staff_gun,
                "is_user": req_user.is_user,
                "is_superuser":req_user.is_superuser,
                "fullname": req_user.fullname,
                "email": req_user.email,
                "phone": req_user.phone,
                "address": req_user.address,
                "cmnd": req_user.cmnd
            }
            return Response(res, 200)
        except Exception as e:
            return Response({
                "Error": repr(e)
            }, 400)

class LoggingViewSet(viewsets.ModelViewSet):
    queryset = Logging.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = LoggingSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = Logging.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def get_logging(self, request):
        res={}
        try:
            users = User.objects.all()
            logging = Logging.objects.all()
            res = {
                "date": datetime.date.today(),
                "user": [
                    logg.user.id
                for logg in logging 
                if str(datetime.date.today()) == str(logg.date_logging.strftime('%Y-%m-%d'))]
            }
            return Response(res, 200)
        except Exception as e:
            return Response({
                "Error": repr(e)
            }, 400)