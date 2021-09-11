from rest_framework import serializers
from django.contrib.auth import get_user_model
from photolair.models import Image

User = get_user_model()


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializer for image model for uploading/downloading images, updating image 
    info and handling transcations 
    """
    class Meta:
        model = Image
        fields = (
          'id',
          'user',
          'image_name',
          'image',
          'inventory',
          'price',
        )
        read_only_fields = ('id',)
    
    def to_representation(self, instance):
        """
        Return only id of associated user
        """
        response = super().to_representation(instance)
        response['user'] = { 
            'id': instance.user.id, 
        }
        return response


class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Serializer for user model to register a new user
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
          'id',
          'username', 
          'password'
        )
        read_only_fields = ('id',)
    
    def create(self, validated_data):
        """
        Create a new user instance, where password is automatically hashed by
        Django via set_password call and stored as hashed value.
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user model provides user details about user such as id,
    and account balance.
    """

    class Meta:
        model = User
        fields = (
          'id',
          'credits',
          'is_staff',
        )
        read_only_fields = ('id',)