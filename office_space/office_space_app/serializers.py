from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('employee_name', 'email_id', 'location_code', 'building_code', 'floor_code', 'user_role')
    # employee_name = serializers.CharField(max_length=100)
    # email_id = serializers.CharField(max_length=100)
    # password = serializers.CharField(max_length=255)
    # location_code = serializers.CharField(max_length=5)
    # building_code = serializers.CharField(max_length=5)
    # floor_code = serializers.CharField(max_length=5)
    # user_role = serializers.CharField(max_length=45, choices=USER_ROLE)

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.employee_name = validated_data.get('employee_name', instance.employee_name)
    #     instance.email_id = validated_data.get('email_id', instance.email_id)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.location_code = validated_data.get('location_code', instance.location_code)
    #     instance.building_code = validated_data.get('building_code', instance.building_code)
    #     instance.floor_code = validated_data.get('floor_code',instance.floor_code)
    #     instance.user_role = validated_data.get('user_role',instance.user_role)
    #     instance.save()
    #     return instance

