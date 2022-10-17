import profile
from xmlrpc.client import ResponseError
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'user_permissions']
        extra_kwargs =  {
            'id' : {'read_only' : True},
            'username' : {'write_only' : True} ,
            'password' : {'write_only' : True} ,
            'is_superuser' : {'write_only' : True} ,
            'is_staff' : {'write_only' : True} ,            
            'user_permissions' : {'write_only' : True} ,
            'last_login' : {'read_only' : True} ,
            'groups' : {'write_only' : True}
        }       
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs =  {
        'id' : {'read_only' : True},            
        'password' : {'write_only' : True, 'required' : False}            
    }              
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:        
        model = Profile
        fields = ['profile_picture', 'user'] 

    def create(self, validated_data):        
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile
       


class ProfileDetailSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()
    class Meta:
        model = Profile
        fields = ['profile_picture', 'user']

    def update(self, instance, validated_data):      
        user_data = validated_data.pop('user') 
        
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)        
        instance.save()
        return instance

        
        
       