from rest_framework import serializers
from .models import detectConnectionError

class detectConnectionErrorSerializer(serializers.Serializer):
    systemList = serializers.JSONField()
    connectionList = serializers.JSONField()
    packages = serializers.JSONField()

    class Meta:
        model = detectConnectionError
        fields = ['systemList', 'connectionList', 'packages']
        
    def create(self, validated_data):
        """
        Create and return a new `detectConnectionError` instance, given the validated data.
        """
        return detectConnectionError(**validated_data)
