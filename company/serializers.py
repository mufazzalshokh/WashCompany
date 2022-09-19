from rest_framework import serializers

from company.models import CompanyModel


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ['name', 'location']
