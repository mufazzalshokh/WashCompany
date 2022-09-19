from rest_framework import serializers


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        # model = JournalModel
        fields = ['name', 'location']
