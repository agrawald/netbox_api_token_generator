from django.contrib.auth import authenticate
from rest_framework import parsers, renderers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import Token
from . import serializers

class ApiLoginView(ObtainAuthToken):

    serializer_class = serializers.ApiLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        username, password, expires = serializer.validated_data['username'], serializer.validated_data['password'], serializer.validated_data['expires']
        
        user = authenticate(request=request, username=username, password=password)
        if user is None:
            raise AuthenticationFailed(detail="Wrong username or password")
        # remove all expired tokens
        for token in Token.objects.filter(user=user):
            if token.is_expired:
                token.delete()
        token, created = Token.objects.get_or_create(user=user, expires=expires)
        return Response({'token': token.key})
