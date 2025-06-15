from rest_framework import serializers
from .models import UserInfo, Contact


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserInfo
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Contact
        fields = '__all__'
