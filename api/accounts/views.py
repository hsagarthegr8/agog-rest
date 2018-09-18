from rest_framework import generics

from .serializers import UserSerializer, VerificationSerializer
from accounts.models import User, Verification


class UserList(generics.ListAPIView):
    """
    List All Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VerificationList(generics.ListAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer


