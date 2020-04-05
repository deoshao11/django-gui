from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets

import requests
import uuid

from .serializer import AccountBalanceSerializer, ExternalAccountSerializer, InternalAccountSerializer

from .models import AccountBalance, ExternalAccount, InternalAccount


def index(request):
    return render(request, 'index.html')


def get_internal_queryset(request):
    username = request.user.username
    print(username)
    r = requests.get(settings.EXTERNAL_API_URL + 'accounts/internal', headers={'x-username': username},)
    json = r.json()
    request_uuid = uuid.uuid4()
    for i in range(len(json)):
        json[i]['requestUuid'] = request_uuid
    serializer = InternalAccountSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return InternalAccount.objects.all().filter(requestUuid=request_uuid)


def get_external_queryset(request):
    username = request.user.username
    r = requests.get(settings.EXTERNAL_API_URL + 'accounts/external', headers={'x-username': username},)
    json = r.json()
    request_uuid = uuid.uuid4()
    for i in range(len(json)):
        json[i]['requestUuid'] = request_uuid
    serializer = ExternalAccountSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return ExternalAccount.objects.all().filter(requestUuid=request_uuid)


def get_balance_queryset(request):
    username = request.user.username
    r = requests.get(settings.EXTERNAL_API_URL + 'account_balance', headers={'x-username': username},)
    json = r.json()
    request_uuid = uuid.uuid4()
    for i in range(len(json)):
        json[i]['requestUuid'] = request_uuid
    serializer = AccountBalanceSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return AccountBalance.objects.all().filter(requestUuid=request_uuid)


class InternalAccountViewSet(viewsets.ModelViewSet):
    serializer_class = InternalAccountSerializer

    def get_queryset(self):
        return get_internal_queryset(self.request)


class ExternalAccountViewSet(viewsets.ModelViewSet):
    serializer_class = ExternalAccountSerializer

    def get_queryset(self):
        return get_external_queryset(self.request)


class AccountBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = AccountBalanceSerializer

    def get_queryset(self):
        return get_balance_queryset(self.request)
