from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', views.NotesViewSet, basename="notes")

urlpatterns = router.urls
