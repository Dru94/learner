from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from exapi.settings import DEFAULT_AUTO_FIELD

from worknotes.serializers import NotesSerializer
from . models import Notes


# Create your views here.
class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    lookup_field = 'slug'
