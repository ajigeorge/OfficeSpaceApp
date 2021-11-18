from django.urls import path, include
from .import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users',views.UserViewSet)


urlpatterns = [
    # path('',include(router.urls)),
    # path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
    path('users/',views.user_list),
    path('users/<int:pk>/',views.user_detail),
    path('',views.index, name = 'home')
]