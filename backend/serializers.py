from rest_framework import serializers
from .models import Listing, ListingImage
from django.contrib.auth.models import User


fields = [
        'id','owner','transaction','rent_period','currency','price',
        'home_type','year_built','area','lot_size','floor','number_of_floors','number_of_rooms','furnishing',
        'street_building','district', 'lat', 'lng',
        'air_conditioning','washing_machine','central_heating','gas','free_wifi','pwd_accessable','elevator','garage','pool',
        'description', 'created',
        'images']

class ListingImageSerializer(serializers.ModelSerializer):
    image_medium = serializers.ImageField(read_only=True)
    class Meta:
        model = ListingImage
        fields = ['id', 'image_medium']

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class ListingSerializer(serializers.ModelSerializer):
    images = ListingImageSerializer(source='listingimage_set', many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = fields

        extra_kwargs = {}
    
    def create(self, validated_data):
        listing = Listing.objects.create(**validated_data)
        images_data = self.context.get('view').request.FILES
        if images_data:
            for image_data in images_data.values():
                ListingImage.objects.create(listing=listing, image_medium=image_data)
        return listing

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key != 'owner' or key != 'images':
                setattr(instance, key, value)
        instance.save()

        images_data = self.context.get('view').request.FILES
        if images_data:
            for image_data in images_data.values():
                ListingImage.objects.create(listing=instance, image_medium =image_data)

        delete_image_data = self.context.get('view').request.data.getlist('to_delete')
        if delete_image_data[0]:
            delete_image_data = delete_image_data[0].split(',')
            for image_id in delete_image_data:
                instance.listingimage_set.get(pk=image_id).delete()
            
        return instance 