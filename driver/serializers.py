from rest_framework import serializers
from .models import Truck, Driver

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['number_plate', 'registration_number']

class DriverSerializer(serializers.ModelSerializer):
    assigned_truck = TruckSerializer()

    class Meta:
        model = Driver
        fields = ['name', 'mobile_number', 'email', 'city', 'district', 'language', 'assigned_truck']



class DriverCreateSerializer(serializers.ModelSerializer):
    truck = TruckSerializer(required=False)

    class Meta:
        model = Driver
        fields = ['name', 'mobile_number', 'email', 'city', 'district', 'language', 'assigned_truck', 'truck']
        
    def validate_mobile_number(self, value):
        if Driver.objects.filter(mobile_number=value).exists():
            raise serializers.ValidationError('mobile number already exists')
        return value
    

    def validate_email(self, value):
        if Driver.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value

    def create(self, validated_data):
        truck_data = validated_data.pop('truck', None)
        assigned_truck = validated_data.get('assigned_truck')

        if not assigned_truck and not truck_data:
            raise serializers.ValidationError("Either 'assigned_truck' or 'truck' data must be provided.")

        if not assigned_truck and truck_data:
            truck_serializer = TruckSerializer(data=truck_data)
            truck_serializer.is_valid(raise_exception=True)
            truck = truck_serializer.save()
            validated_data['assigned_truck'] = truck

        driver = Driver.objects.create(**validated_data)
        return driver

    

