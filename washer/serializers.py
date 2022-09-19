from rest_framework import serializers

from washer.models import WasherModel


class WasherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasherModel
        fields = ['name', 'location']
