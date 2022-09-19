from django.db import models
from django.db.models import CASCADE

from company.models import CompanyModel


class UserModel(models.Model):
    name = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    role_admin = models.BooleanField(default=False)
    role_owner = models.BooleanField(default=False)
    user = models.ForeignKey(CompanyModel, on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
