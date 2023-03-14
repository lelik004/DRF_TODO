
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from todo.views import ProjectModelViewSet, ToDoModelViewSet
from usersapp.views import CustomUserModelViewSet
from usersapp.views_example_lesson4 import UserApiView, users_apiview,\
    UserCreateGenericView, UserListGenericView, UserRetrieveGenericView, UserDestroyGenericView, UserUpdateGenericView,\
    UserRetrieveUpdateDestroyGenericView, UserViewSet


router = DefaultRouter()
router.register('users', CustomUserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)
router.register('user_for_lvl3', UserViewSet, basename='user_for_lvl3')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # APIView. lesson_4
    path('api/user/', UserApiView.as_view()),

    # @api_view
    path('api/user/decorapiview', users_apiview),

    # GenericAPIView
    path('generic/create/', UserCreateGenericView.as_view()),
    path('generic/list/', UserListGenericView.as_view()),
    path('generic/retrieve/<int:pk>', UserRetrieveGenericView.as_view()),
    path('generic/destroy/<int:pk>', UserDestroyGenericView.as_view()),
    path('generic/update/<int:pk>', UserUpdateGenericView.as_view()),
    path('generic/retrive_update_destroy/<int:pk>', UserRetrieveUpdateDestroyGenericView.as_view()),

    # ViewSet
    path('viewsets/', include(router.urls)),

]



