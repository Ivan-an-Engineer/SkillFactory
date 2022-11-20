from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "fam", "name", "otc", "phone"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'data', 'title']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['id', 'pereval', 'latitude', 'longitude', 'height']


class PerevalSerializer(serializers.ModelSerializer):
    coords = CoordsSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'level_winter', 'level_summer',
                  'level_autumn', 'level_spring', 'coords', 'images']

    def create(self, validated_data):
        pereval = Pereval.objects.create(**validated_data)
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')
        Coords.object.create(pereval=pereval, **coords_data)
        for image_data in images_data:
            image = Image.object.create(**image_data)
            PerevalImage.object.create(foto=image, pereval=pereval)
        return pereval




