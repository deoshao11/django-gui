from django.db import models

# Create your models here.


class InternalAccount(models.Model):
    accountName = models.CharField(max_length=100)
    sourceId = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    productAssociation = models.CharField(max_length=100)
    externalAccountAssociation = models.CharField(max_length=100)

    def __str__(self):
        return self.accountName


class ExternalAccount(models.Model):
    accountName = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    exchangeAssociation = models.CharField(max_length=100)

    def __str__(self):
        return self.accountName
