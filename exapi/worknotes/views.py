from django.shortcuts import render
from rest_framework import viewsets, status, generics, renderers
from rest_framework.permissions import AllowAny
from exapi.settings import DEFAULT_AUTO_FIELD
from rest_framework import filters
from rest_framework.decorators import action
from django.http import FileResponse, HttpResponse
from wsgiref.util import FileWrapper

from worknotes.serializers import NotesSerializer
from . models import Notes


# Create your views here.


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject', 'topic']


class FileDownloadView(generics.ListAPIView):
    def get(self, request, id, format=None):
        ext = ""
        queryset = Notes.objects.get(id=id)
        for char in reversed(queryset.notes.name):
            if char != ".":
                ext += char
            else:
                break

        ext = ext[::-1]
        doc = queryset.notes.path
        document = open(doc, 'rb')
        response = HttpResponse(FileWrapper(document),
                                content_type="application/"+ext)
        return response
