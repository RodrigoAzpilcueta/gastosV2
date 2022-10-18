from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model =  User
        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff'            
        ]
        extra_kwargs = {
            'username' : {'write_only' : True},
            'password' : {'write_only' : True},
            'is_active' : {'write_only' : True},
            'is_staff' : {'write_only' : True}
        } 

class UserUpdateSerializer(serializers.ModelSerializer):   

    class Meta:
        model =  User
        fields = [
            'id',            
            'password',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff'            
        ]
        extra_kwargs = {
            'username' : {'write_only' : True},
            'password' : {'write_only' : True, 'required' : False},
            'is_active' : {'write_only' : True},
            'is_staff' : {'write_only' : True}
        } 
   
class ProfileSerializer(serializers.ModelSerializer):             
    user = UserSerializer()
    wallets = serializers.StringRelatedField(many=True)
    class Meta:        
        model = Profile
        fields = ['profile_picture', 'user', 'wallets'] 

    def create(self, validated_data):        
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)        
        return profile
       

class ProfileUpdateSerializer(serializers.ModelSerializer):     
    
    user = UserUpdateSerializer()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('a')
        if 'view' in self.context and self.context['view'].action in ['update', 'partial_update']:
            print('b')
            print(self.context)
            self.fields.pop('username', None)
    

    class Meta:        
        model = Profile
        fields = ['profile_picture', 'user'] 

    def update(self,  instance, validated_data):        
        user_data = validated_data.pop('user')
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)        
        instance.save()
        return instance

        
        
       