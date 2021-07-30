from rest_framework import serializers
from rest_framework.exceptions import ParseError

class ApiLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    expires  =serializers.CharField()

    def validate(self, attrs):
        if attrs is None:
            raise ParseError(detail='Empty request')
        if not attrs.get('username'):
            raise ParseError(detail='Missing username')
        if not attrs.get('password'):
            raise ParseError(detail='Missing password')
        if not attrs.get('expires'):
            raise ParseError(detail='Missing expires')
        return attrs