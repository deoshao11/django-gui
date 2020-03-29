from django.shortcuts import render

from rest_framework import viewsets
import requests

from .serializer import InternalAccountSerializer
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')


def get_internal_account(request):
    r = requests.get('http://sunyi-lonk-spec.herokuapp.com/accounts/internal')
    json = r.json()
    print(json)
    serializer = InternalAccountSerializer(data=json, many=True)
    print(serializer.is_valid())
    print(serializer.errors)
    accounts = serializer.save()
    return render(request, 'accounts.html', {'accounts': accounts})


class InternalAccountViewSet(viewsets.ViewSet):
    def list(self, request):
        r = requests.get('http://sunyi-lonk-spec.herokuapp.com/accounts/internal')
        json = r.json()
        return Response(json)


class ExternalAccountViewSet(viewsets.ViewSet):
    def list(self, request):
        r = requests.get('http://sunyi-lonk-spec.herokuapp.com/accounts/external')
        json = r.json()
        return Response(json)
