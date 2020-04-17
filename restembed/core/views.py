from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
import base64

import requests
import uuid

from .serializer import *

from .models import *
from Crypto.Cipher import AES
import dateutil.parser

def index(request):
    return render(request, 'index.html')


def get_data_from_api_call(request, endpoint, params={}):
    username = request.user.username
    encrypted_username = get_encryption(username)
    r = requests.get(settings.EXTERNAL_API_URL + endpoint,
                     headers={'x-encrypted-username': encrypted_username}, params=params)
    json = r.json()
    request_uuid = uuid.uuid4()
    for i in range(len(json)):
        json[i]['requestUuid'] = request_uuid
        if endpoint == 'transfer':
            json[i]['transferID'] = json[i]['id']
    return json, request_uuid

def get_internal_queryset(request):
    json, request_uuid = get_data_from_api_call(request, 'accounts/internal')
    serializer = InternalAccountSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return InternalAccount.objects.all().filter(requestUuid=request_uuid)


def get_external_queryset(request):
    json, request_uuid = get_data_from_api_call(request, 'accounts/external')
    serializer = ExternalAccountSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return ExternalAccount.objects.all().filter(requestUuid=request_uuid)


def get_balance_queryset(request):
    json, request_uuid = get_data_from_api_call(request, 'account_balance')
    serializer = AccountBalanceSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return AccountBalance.objects.all().filter(requestUuid=request_uuid)


def get_transfer_queryset(request):
    start_time = int(dateutil.parser.parse(request.query_params.get('startTime')).timestamp() * 1000)
    end_time = int(dateutil.parser.parse(request.query_params.get('endTime')).timestamp() * 1000)
    print(start_time, end_time)
    params = {'startTime': start_time, 'endTime': end_time}
    json, request_uuid = get_data_from_api_call(request, 'transfer', params)
    serializer = TransferSerializer(data=json, many=True)
    if not serializer.is_valid():
        print(serializer.errors)
    serializer.save()
    return Transfer.objects.all().filter(requestUuid=request_uuid)


def get_encryption(username):
    secret_key = settings.ENCRYPTION_SECRET_KEY.encode('utf-8')
    iv_key = settings.ENCRYPTION_IV_KEY.encode('utf-8')
    encryptor = AES.new(secret_key, AES.MODE_CBC, iv_key)
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    encrypted_username = base64.b64encode(encryptor.encrypt(pad(username)))
    return encrypted_username


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


class TransferViewSet(viewsets.ModelViewSet):
    serializer_class = TransferSerializer

    def get_queryset(self):
        return get_transfer_queryset(self.request)
