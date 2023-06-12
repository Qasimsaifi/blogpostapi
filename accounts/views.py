from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer

class UserDetailView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        data = {
            'email': user.email,
            'mobile': user.mobile,
            'profile_picture': user.profile_picture.url if user.profile_picture else None,
            'name': {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'full_name': user.first_name + " " + user.last_name
            }
        }
        return Response(data)
