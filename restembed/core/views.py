from itertools import chain

from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
import requests

from .serializer import AccountBalanceSerializer, ExternalAccountSerializer, InternalAccountSerializer

from .models import AccountBalance, ExternalAccount, InternalAccount


def index(request):
    return render(request, 'index.html')


def get_internal_queryset():
    r = requests.get(settings.EXTERNAL_API_URL + 'accounts/internal')
    json = r.json()
    serializer = InternalAccountSerializer(data=json, many=True)
    print(serializer.is_valid())
    print(serializer.errors)
    serializer.save()
    return InternalAccount.objects.all()


def get_external_queryset():
    r = requests.get(settings.EXTERNAL_API_URL + 'accounts/external')
    json = r.json()
    serializer = ExternalAccountSerializer(data=json, many=True)
    print(serializer.is_valid())
    print(serializer.errors)
    serializer.save()
    return ExternalAccount.objects.all()


def get_balance_queryset():
    r = requests.get(settings.EXTERNAL_API_URL + 'account_balance')
    json = r.json()
    print(json)
    serializer = AccountBalanceSerializer(data=json, many=True)
    print(serializer.is_valid())
    print(serializer.errors)
    serializer.save()
    return AccountBalance.objects.all()


class InternalAccountViewSet(viewsets.ModelViewSet):
    queryset = get_internal_queryset()
    serializer_class = InternalAccountSerializer


class ExternalAccountViewSet(viewsets.ModelViewSet):
    queryset = get_external_queryset()
    serializer_class = ExternalAccountSerializer


class AccountBalanceViewSet(viewsets.ModelViewSet):
    queryset = get_balance_queryset()
    serializer_class = AccountBalanceSerializer
# class AccountBalanceViewSet(viewsets.ViewSet):
#     def list(self, request):
#         r = requests.get(settings.EXTERNAL_API_URL + 'account_balance')
#         json = r.json()
#         print(json)
#         return Response(json)
