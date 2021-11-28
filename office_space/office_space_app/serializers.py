from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('employee_name', 'email_id', 'location_code', 'building_code', 'floor_code', 'user_role')

