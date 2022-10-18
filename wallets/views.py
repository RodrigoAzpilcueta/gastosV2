from django.shortcuts import render

from .serializers import WalletSerializer
from rest_framework import viewsets

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class =  WalletSerializer
    queryset = WalletSerializer.Meta.model.objects.all()