from django.db.models import fields
from rest_framework import serializers
from .models import Notes
from exapi.settings import MEDIA_URL


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
