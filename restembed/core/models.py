from django.db import models
from jsonfield import JSONField

# Create your models here.


class InternalAccount(models.Model):
    accountName = models.CharField(max_length=100)
    sourceId = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    productAssociation = models.CharField(max_length=100)
    externalAccountAssociation = models.CharField(max_length=100)
    requestUuid = models.UUIDField()
    children = JSONField()
    hasParents = models.BooleanField()

    def __str__(self):
        return self.accountName


class ExternalAccount(models.Model):
    accountName = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    exchangeAssociation = models.CharField(max_length=100)
    requestUuid = models.UUIDField()

    def __str__(self):
        return self.accountName


class AccountBalance(models.Model):
    accountName = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    instruments = JSONField()
    requestUuid = models.UUIDField()

    def __str__(self):
        return self.accountName


class Transfer(models.Model):
    transferID = models.BigIntegerField()
    time = models.BigIntegerField()
    status = models.CharField(max_length=100)
    msg = models.CharField(max_length=100, blank=True)
    requestUuid = models.UUIDField()

    def __str__(self):
        return self.transferID