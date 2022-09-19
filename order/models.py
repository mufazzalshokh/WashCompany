from django.db import models
from django.db.models import CASCADE

from company.models import CompanyModel


class OrderModel(models.Model):
    # id,set = service ?
    # set = models.ForeignKey(WasherModel)
    price = models.IntegerField()
    carModel = models.CharField(max_length=30)
    carNumber = models.CharField(max_length=3)
    clientName = models.CharField(max_length=50)
    clientNumber = models.IntegerField()
    isActive = models.BooleanField()
    isCancelled = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(CompanyModel, on_delete=CASCADE)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
