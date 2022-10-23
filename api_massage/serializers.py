from rest_framework import serializers
from website.models import Service, Recording, User


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('service', 'text', 'duration', 'price')


class RecordsSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Recording
        fields = ('service', 'customer', 'date_of_the_service')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'gender', 'email')
