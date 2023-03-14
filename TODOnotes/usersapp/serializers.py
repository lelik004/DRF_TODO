from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        # fields = ('first_name', 'last_name', 'email',)
        fields = ('pk', 'username', 'first_name', 'last_name', 'email',)

    def __str__(self):
        return f'{self.first_name}'



