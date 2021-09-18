from rest_framework import serializers

from photolair.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializer for image model used for uploading/downloading images 
    and handling transcations 
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
            'username': instance.user.username,
        }
        return response


class ImageUpdateSerialier(serializers.ModelSerializer):
    """
    Serializer for image model used to update image and image details 
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
        read_only_fields = ('id','user')
        extra_kwargs = {
            'image_name': {'required': False},
            'image': {'required': False},
            'inventory': {'required': False},
            'price': {'required': False},
        }
    
    def to_representation(self, instance):
        """
        Return only id of associated user
        """
        response = super().to_representation(instance)
        response['user'] = {
            'username': instance.user.username,
        }
        return response
