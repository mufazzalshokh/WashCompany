from django.db import models
from django.db.models import CASCADE

from company.models import CompanyModel


class WasherModel(models.Model):
    name = models.CharField(max_length=30)
    telephoneNumber = models.IntegerField()
    stake = models.IntegerField()
    image = models.ImageField()
    is_active = models.BooleanField()
    washer = models.ForeignKey(CompanyModel, on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'washer'
        verbose_name_plural = 'washers'
