from rest_framework import serializers
from .models import *


class InternalAccountSerializer(serializers.ModelSerializer):
    children = serializers.JSONField()

    class Meta:
        model = InternalAccount
        fields = '__all__'


class ExternalAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalAccount
        fields = '__all__'


class AccountBalanceSerializer(serializers.ModelSerializer):
    instruments = serializers.JSONField()

    class Meta:
        model = AccountBalance
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'