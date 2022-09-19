from django.db import models
from django.db.models import CASCADE

from company.models import CompanyModel


class ServiceModel(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    price = models.IntegerField()
    service = models.ForeignKey(CompanyModel, on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'
