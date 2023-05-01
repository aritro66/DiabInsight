from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializer
from .models import Users
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.authtoken.models import Token
import jwt
import datetime
from .middlewares import CustomMiddleware
from django.utils.decorators import decorator_from_middleware
auth_decorator = decorator_from_middleware(CustomMiddleware)

def generate_access_token(user):

    access_token_payload = {
        'user_id': user['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              "huhuha", algorithm='HS256')
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, "huhuha", algorithm='HS256')

    return refresh_token


@api_view(['POST'])
def adduser_list(request):

    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = Users.objects.get(id=serializer.data['id'])
            print(serializer.data, user)
            
            token = generate_access_token(serializer.data)
            refreshtoken = generate_refresh_token(serializer.data)
            return Response({'data':serializer.data, 'AccessToken':token, 'RefreshToken': refreshtoken}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@auth_decorator    
@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
