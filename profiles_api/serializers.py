from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing APIView"""
    # Create a new name character field on serializer that allows input
    name = serializers.CharField(max_length=10)