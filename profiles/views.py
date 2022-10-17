from turtle import st
from .models import Profile
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, ProfileDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ProfileList(APIView):
    
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
        

class ProfileDetail(APIView):

     def get(self, request, pk):
        profiles = Profile.objects.get(pk=pk)
        serializer = ProfileDetailSerializer(profiles, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

     def put(self, request, pk):        
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileDetailSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
