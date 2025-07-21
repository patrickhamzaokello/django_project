from django.shortcuts import render
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileListCreate(generics.ListCreateAPIView):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileSerializer
