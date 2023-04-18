from rest_framework import serializers
from prices.models import Token


class TokenSerializer(serializers.ModelSerializer):
    '''The only API serializer'''
    class Meta:
        model = Token
        fields = '__all__'