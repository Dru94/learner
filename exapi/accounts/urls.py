from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.UserViewSet, basename='user-list')

urlpatterns = router.urls
