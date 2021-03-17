from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'password_confirmation')
        extra_kwargs = {
        'first_name': {'allow_blank': False, 'required': True},
        'last_name': {'allow_blank': False, 'required': True},
        'email': {'allow_blank': False, 'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": "Password fields did not match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user