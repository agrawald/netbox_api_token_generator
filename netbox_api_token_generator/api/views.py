from django.contrib.auth import authenticate
from rest_framework import parsers, renderers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import AuthenticationFailed, ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import Token
from . import serializers
import base64

class ApiLoginView(ObtainAuthToken):


    def get(self, request, *args, **kwargs):
        authorization = request.headers.get("Authorization")
        if(authorization is None or len(authorization) <=0):
            raise ParseError("Invalid Authorization header.")
        print(authorization)

        expires = request.headers.get("X-Expires")
        if(expires is None or len(expires) <=0):
            raise ParseError("Invalid X-Expires header.")
        print(expires)

        username, password = self.extractUsernamePassword(request.headers.get("Authorization"))
        
        user = authenticate(request=request, username=username, password=password)
        if user is None:
            raise AuthenticationFailed(detail="Wrong username or password")
        # remove all expired tokens
        for token in Token.objects.filter(user=user):
            if token.is_expired:
                token.delete()
        token, created = Token.objects.get_or_create(user=user, expires=expires)
        return Response({'token': token.key})

    def extractUsernamePassword(self, auth_header):
        auth_arr = auth_header.split()

        if(len(auth_arr) < 2):
            raise ParseError(detail="Invalid Authorization header provided")

        encoded = auth_arr[1]
        print(encoded)
        decoded = self.decode(encoded).split(":")
        print(decoded)
        
        if(len(decoded) < 2):
            raise ParseError(detail="Invalid Authorization encoding ")

        return decoded[0], decoded[1]

    def decode(self, encoded):
        base64_bytes = encoded.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode('ascii')


