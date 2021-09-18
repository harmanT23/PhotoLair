from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


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
            'credits', 
            'password'
        )
        read_only_fields = ('id', 'credits')
    
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
            'username',
            'credits',
            'is_staff',
        )
        read_only_fields = ('id', 'credits')
        