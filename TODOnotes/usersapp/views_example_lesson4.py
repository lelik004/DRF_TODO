from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView, get_object_or_404


from .models import CustomUser
from .serializers import CustomUserSerializer




# 1. APIView. lesson_4
class UserApiView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)


# 2. @api_view

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def users_apiview(request):
    user = CustomUser.objects.all()
    serializer = CustomUserSerializer(user, many=True)
    return Response(serializer.data)


# 3. GenericAPIView
# Create
class UserCreateGenericView(CreateAPIView):
    # renderer_classes = [BrowsableAPIRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# List
class UserListGenericView(ListAPIView):
    # renderer_classes = [AdminRenderer]
    # renderer_classes = [AdminRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Retrieve
class UserRetrieveGenericView(RetrieveAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Destroy
class UserDestroyGenericView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Update
class UserUpdateGenericView(UpdateAPIView):
    # renderer_classes = [AdminRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# RetrieveUpdateDestroyAPIView
class UserRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    # renderer_classes = [AdminRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# 3. ViewSet
class UserViewSet(ViewSet):
    # renderer_classes = [JSONRenderer]

    @action(detail=True, methods=['get'])
    def username_only(self, request, pk=None):
        user = get_object_or_404(CustomUser, pk=pk)
        return Response({'user.username': user.username})

    def list(self, request):
        user = CustomUser.objects.all()
        serializer_class = CustomUserSerializer(user, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer_class = CustomUserSerializer(user)
        return Response(serializer_class.data)
