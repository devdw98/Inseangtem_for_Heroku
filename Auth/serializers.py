from rest_framework.serializers import ModelSerializer
from .models import IstUser

class IstUserSerializer(ModelSerializer):
    class Meta:
        model = IstUser
        fields = ['pk','username']
    