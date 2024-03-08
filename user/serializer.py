from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        fields=["full_name","phone_number","email","password"]
        model=CustomUser
        # read_only_fields = ['email']
        

