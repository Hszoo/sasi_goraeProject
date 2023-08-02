from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from posts.models import UserInfo

class UserInfoSerializer(ModelSerializer) :
    user = serializers.ReadOnlyField(source='user.username')

    class Meta : 
        model = UserInfo
        fields = '__all__'


class UserSerializer(ModelSerializer) :
    userInfo = serializers.SerializerMethodField()
    def create(self, validated_data) :
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
        )
        return user
    class Meta :
        model = User
        fields = ['id', 'username', 'password', 'email', 'userInfo']

    def get_userInfo(self, user) :
        try : 
            userInfo = UserInfo.objects.get(user=user)
            return UserInfoSerializer(userInfo).data
        except UserInfo.DoesNotExist:
            return None 

class MypageSerializer(ModelSerializer) :
    user = serializers.ReadOnlyField(source='user.username')

    class Meta : 
        model = UserInfo
        fields = ['user', 'nickname', 'profile', 'points', 'count']    

