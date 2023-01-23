from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(['POST'])
def register(request):
    data = request.data

    email = data['email']
    username  = data["username"]
    password = data["password"]
    password2 = data['password2']

    if User.objects.filter(email=email).exists():
        return Response({"message" : "User with this email already exists "}, status=status.HTTP_400_BAD_REQUEST)

    elif len(username) < 3:
        return Response({"message" : "Username should contais at least 3 characters "},status=status.HTTP_400_BAD_REQUEST)

    elif password != password2:
        return Response({
            "message" : "Passwords do not match "
        },status=status.HTTP_400_BAD_REQUEST)
    elif len(password) < 6:
        return Response({
            "message" : "A strong password contains at least 6 characters "
        },status=status.HTTP_400_BAD_REQUEST)

    else:
        user  = User.objects.create_user(
            email=email, 
            username=username,
            password=password
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def load_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)