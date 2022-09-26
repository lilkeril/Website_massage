from rest_framework import serializers
from website.models import Service, Recording, User


# class RecordsSerializer(serializers.Serializer):
#     service_id = serializers.IntegerField()
#     customer_id = serializers.IntegerField()
#     date_of_the_service = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Recording.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.service_id = validated_data.get('service_id', instance.service_id)
#         instance.customer_id = validated_data.get('customer_id', instance.customer_id)
#         instance.date_of_the_service = validated_data.get('date_of_the_service', instance.date_of_the_service)
#         instance.save()
#         return instance
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('service', 'text', 'duration', 'price')


class RecordsSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Recording
        fields = ('service', 'customer', 'date_of_the_service')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'lastname', 'gender', 'email')








