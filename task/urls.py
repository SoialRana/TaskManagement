from django.urls import path,include
from rest_framework import routers
from . views import TaskViewSet#,PhotoViewSet
router=routers.DefaultRouter()
router.register('first_tasks',TaskViewSet,basename='task')
# router.register(r'photo',PhotoViewSet,basename='photo')

urlpatterns = [
    path('',include(router.urls)),
    path('api/',include('rest_framework.urls')),
]
