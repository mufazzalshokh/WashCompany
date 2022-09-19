from django.db import models


class CompanyModel(models.Model):
    name = models.CharField(max_length=30)
    avatar = models.ImageField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
