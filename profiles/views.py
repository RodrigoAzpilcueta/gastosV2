from .serializers import ProfileSerializer, ProfileUpdateSerializer
from rest_framework import viewsets

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class =  ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()

    def get_serializer_class(self): 
        serializer_class = self.serializer_class 
        if self.action == 'update' or self.action == 'partial_update': 
            serializer_class = ProfileUpdateSerializer
        return serializer_class




