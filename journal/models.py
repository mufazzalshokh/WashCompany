from django.db import models


class JournalModel(models.Model):
    orderId = models.IntegerField()
    userName = models.CharField(max_length=30)
    previousCarModel = models.CharField(max_length=30)
    currentCarModel = models.CharField(max_length=30)
    previousCarNumber = models.CharField(max_length=30)
    currentCarNumber = models.CharField(max_length=30)
    previousServicesName = models.CharField(max_length=30)
    currentServicesName = models.CharField(max_length=30)
    previousServicesPrice = models.CharField(max_length=30)
    currentServicesPrice = models.CharField(max_length=30)
    previousPrice = models.CharField(max_length=30)
    currentPrice = models.CharField(max_length=30)
    isCancelled = models.BooleanField(max_length=30)
    cancelledReason = models.CharField(max_length=30)
