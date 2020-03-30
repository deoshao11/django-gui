from itertools import chain

from django.shortcuts import render

from rest_framework import viewsets
import requests

from .serializer import ExternalAccountSerializer, InternalAccountSerializer

from .models import ExternalAccount, InternalAccount


def index(request):
    return render(request, 'index.html')


def get_internal_queryset():
    r = requests.get('http://sunyi-lonk-spec.herokuapp.com/accounts/internal')
    json = r.json()
    #print(json)
    serializer = InternalAccountSerializer(data=json, many=True)
    print(serializer.is_valid())
    serializer.save()
    return InternalAccount.objects.all()


def get_external_queryset():
    r = requests.get('http://sunyi-lonk-spec.herokuapp.com/accounts/external')
    json = r.json()
    serializer = ExternalAccountSerializer(data=json, many=True)
    print(serializer.is_valid())
    serializer.save()
    return ExternalAccount.objects.all()


class InternalAccountViewSet(viewsets.ModelViewSet):
    queryset = get_internal_queryset()
    serializer_class = InternalAccountSerializer


class ExternalAccountViewSet(viewsets.ModelViewSet):
    queryset = get_external_queryset()
    serializer_class = ExternalAccountSerializer
