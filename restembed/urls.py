"""restembed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from .core.views import AccountBalanceViewSet, ExternalAccountViewSet, InternalAccountViewSet, index

from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'internal', InternalAccountViewSet, basename='internal_account')
router.register(r'external', ExternalAccountViewSet, basename='external_account')
router.register(r'balance', AccountBalanceViewSet, basename='account_balance')

urlpatterns = [
    url('^api/', include(router.urls)),
    url(r'^$', index, name='index'),
    url(r'^login/$', LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
    url(r'^admin/', admin.site.urls),
]
