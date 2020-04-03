from rest_framework import serializers
from .models import AccountBalance, InternalAccount, ExternalAccount


class InternalAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalAccount
        fields = ('accountName', 'sourceId', 'type', 'productAssociation', 'externalAccountAssociation')


class ExternalAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalAccount
        fields = ('accountName', 'type', 'exchangeAssociation')


class AccountBalanceSerializer(serializers.ModelSerializer):
    instruments = serializers.JSONField()

    class Meta:
        model = AccountBalance
        fields = ('accountName', 'instruments', 'type')