
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Logging
from rest_framework.validators import UniqueValidator

from django.conf import settings

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    fullname = serializers.CharField(required=True, allow_blank=True, max_length=100)
    is_staff_gun = serializers.BooleanField(required=True)
    is_user = serializers.BooleanField(required=True)
    phone = serializers.CharField(required=True, allow_blank=True, max_length=12)
    address = serializers.CharField(required=True, allow_blank=True, max_length=20)
    cmnd = serializers.CharField(required=True, allow_blank=True, max_length=12)
    password = serializers.CharField(required=True, allow_blank=True, max_length=100)
    class Meta:
        model = User
        fields = ('fullname', 'is_staff_gun','is_user','phone', 'address', 'cmnd', 'password',
                'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.cmnd = validated_data.get('cmnd', instance.cmnd)
        instance.save()
        return instance

class LoggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logging
        fields = "__all__"