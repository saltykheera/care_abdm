from rest_framework import serializers

from care_abdm.models import HealthFacility


class HealthFacilitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="external_id", read_only=True)
    registered = serializers.BooleanField(read_only=True)

    class Meta:
        model = HealthFacility
        exclude = ("deleted",)
