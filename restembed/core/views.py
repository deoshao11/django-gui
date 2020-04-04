from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets

import requests
import uuid

from .serializer import AccountBalanceSerializer, ExternalAccountSerializer, InternalAccountSerializer

from .models import AccountBalance, ExternalAccount, InternalAccount


def index(request):
    return render(request, 'index.html')


def get_internal_queryset():
    r = requests.get(settings.EXTERNAL_API_URL + 'accounts/internal')
    request_uuid = uuid.uuid4()
    json = r.json()
    for i in range(len(json)):
        json[i]['requestUuid'] = request_uuid
    print(json)
    serializer = InternalAccountSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return InternalAccount.objects.all().filter(requestUuid=request_uuid)


def get_external_queryset():
    r = requests.get(settings.EXTERNAL_API_URL + 'accounts/external')
    json = r.json()
    request_uuid = uuid.uuid4()
    for i in range(len(json)):
        json[i]['requestUuid'] = request_uuid
    print(json)
    serializer = ExternalAccountSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return ExternalAccount.objects.all().filter(requestUuid=request_uuid)


def get_balance_queryset():
    r = requests.get(settings.EXTERNAL_API_URL + 'account_balance')
    json = r.json()
    request_uuid = uuid.uuid4()
    for i in range(len(json)):
        json[i]['requestUuid'] = request_uuid
    print(json)
    serializer = AccountBalanceSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return AccountBalance.objects.all().filter(requestUuid=request_uuid)


class InternalAccountViewSet(viewsets.ModelViewSet):
    queryset = get_internal_queryset()
    serializer_class = InternalAccountSerializer


class ExternalAccountViewSet(viewsets.ModelViewSet):
    queryset = get_external_queryset()
    serializer_class = ExternalAccountSerializer


class AccountBalanceViewSet(viewsets.ModelViewSet):
    queryset = get_balance_queryset()
    serializer_class = AccountBalanceSerializer
