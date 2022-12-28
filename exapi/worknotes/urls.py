from posixpath import basename
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', views.NotesViewSet, basename="notes")


urlpatterns = [
    path('download/<int:id>/', views.FileDownloadView.as_view(), name='notes_download')
] 

urlpatterns += router.urls
