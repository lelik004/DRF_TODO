from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import CustomUser


class CustomUserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'first_name', 'last_name', 'email',)


